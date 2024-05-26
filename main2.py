from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_community.document_loaders import CSVLoader
from dotenv import load_dotenv

load_dotenv()

#Carregar documentos
loader = CSVLoader(file_path='ResourceCosts.csv', encoding='utf-8')
documents = loader.load()

#Criar embeddings
embeddings = OpenAIEmbeddings()


db = FAISS.from_documents(documents, embeddings)

def retrieve_info(query):
    similar_response = db.similarity_search(query, k=3)
    return [doc.page_content for doc in similar_response]

llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo-16k-0613")

template = """
Você é um assistente interno em uma empresa de software.
Sua função é auxiliar os analistas FinOps e de TI em todos os assuntos envolvendo os custos em nuvem. A plataforma utilizada é a Microsoft Azure.
Forneça insights, oportunidades de economia em determinados casos baseado no consumo, sugira reservas de recursos quando aplicável e outras estratégias para otimizar os custos do ambiente.

Aqui está a tabela contendo o custo mensal dos recursos dos últimos 6 meses. Utilize esses dados como base para as respostas.
{table}
Aqui está uma pergunta de um de nossos analistas:
{message}
"""

prompt = PromptTemplate(
    input_variables=["message", "table"],
    template=template
)

#llm = OpenAI()
#chain = prompt | llm

llm = ChatOpenAI()
chain = prompt | llm

def generate_response(message):
    table = retrieve_info(message)
    table_str = "\n".join(table)
    response = chain.invoke({"message": message, "table": table_str})
    return response.content

print(generate_response("Qual é o recurso que mais custou no mes de fevereiro?"))