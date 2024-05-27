# TCC-langchain

Este pequeno código é para utilizar de forma simples o framework Langchain com a API da OpenAI, utilizando o chatgpt 3.5-turbo para auxiliar com no processo de avaliação dos dados de custos na plataforma de nuvem da Azure.

É necessário utilizar a API da OpenAI. Criar uma API Key na plataforma, https://platform.openai.com/api-keys e inserir no arquivo .env para a aplicação utilizar a API.

No contexto, foi utilizada uma tabela em CSV com dados exportados da plataforma Microsoft Azure. Os dados continham o histórico de custos associados aos recursos na plataforma. 
A aplicação realiza a leitura da tabela e a utiliza como base para as respostas, é utilizado o framework de LLM LangChain para toda a interação entre os dados, prompt e LLM.
