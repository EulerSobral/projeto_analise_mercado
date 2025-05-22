# Projeto Analise de Mercado Financeiro

A ideia desse projeto é utilizar sistemas multiagentes para fazer um resumo corporativo sobre determinado mercado ou setor, como, por exemplo, o Tecnologia da Informação.  
Criei três agentes para esse projeto. O primeiro agente, denominado analista de mercado, faz pesquisas sobre determinado setor financeiro retornando dados relevantes sobre o mercado, identificando tendências ,as principais empresas e as pessoas mais influentes desse setor. O segundo agente, denominado analista de tendências, examina os dados coletados pelo agente analista de mercado, identificando padrões, tendências, oportunidades e ameaças para o setor em quesão. O terceiro agente, denominado Redator de mercado, é responsável por gerar um relatório resumido e de fácil compreensão utilizando o modelo de resumo coorporativo sobre as informações fornecidas pelo analista de tendências, ele vai retornar esse relatório em um arquivo do tipo relatorio.html

## Tecnologias Utilizadas no desenvolvimento desse projeto 
- Python 3.13.1
- uv 0.7.5
- crewai 0.120.1
- Sistema Operacional Windows 10
- LLM: gemini/gemini-2.0-flash-lite-001
  
## Instalação das dependências do projeto.

Para o projeto funcionar, é necessário que você utilize alguma LLM por meio de uma api fornecida pela LLM, como, por exemplo, a api do chat gpt. Nesse projeto, 
eu utilize a LLM gemini/gemini-2.0-flash-lite-001, mas você pode se sentir livre em utilizar outra LLM do seu gosto para rodar o projeto. 
Na data em que desenvolvi esse projeto, 20/05/2025, fiz uso da API do Gemini disponibilizada gratuitamente pelo Google. Para acessar a chave da api do Google, [clique aqui](https://aistudio.google.com/0)

Com a sua chave da api, acesse o arquivo do projeto `.env` e cole cahve  da api no seguinte espaço `GEMINI_API_KEY=DIGITE SUA API KEY` 

Caso não tenha o crewai instalado em sua máquina, siga os seguintes procedimentos. 
- Instale o uv
    No MacOs ou Linux: ```bash curl -LsSf https://astral.sh/uv/install.sh | sh ```
    Caso seu sistema não utilize o curl, utilize o seguinte comando ```bash wget -qO- https://astral.sh/uv/install.sh | sh```
    No Windows: ```bash powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"```
- Rodando o projeto
- **OBS: Antes de rodar o projeto, verifique se a sua verção do Python é maior ou equivalente a 3.10**

```bash
crewai install
```

```bash
crewai run
```
### Customizing

**Add your `OPENAI_API_KEY` into the `.env` file**

- Modify `src/projeto_analise_mercado/config/agents.yaml` to define your agents
- Modify `src/projeto_analise_mercado/config/tasks.yaml` to define your tasks
- Modify `src/projeto_analise_mercado/crew.py` to add your own logic, tools and specific args
- Modify `src/projeto_analise_mercado/main.py` to add custom inputs for your agents and tasks

## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
$ crewai run
```

This command initializes the projeto_analise_mercado Crew, assembling the agents and assigning them tasks as defined in your configuration.

This example, unmodified, will run the create a `report.md` file with the output of a research on LLMs in the root folder.

## Understanding Your Crew

The projeto_analise_mercado Crew is composed of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their collective skills to achieve complex objectives. The `config/agents.yaml` file outlines the capabilities and configurations of each agent in your crew.

## Support

For support, questions, or feedback regarding the ProjetoAnaliseMercado Crew or crewAI.
- Visit our [documentation](https://docs.crewai.com)
- Reach out to us through our [GitHub repository](https://github.com/joaomdmoura/crewai)
- [Join our Discord](https://discord.com/invite/X4JWnZnxPb)
- [Chat with our docs](https://chatg.pt/DWjSBZn)

Let's create wonders together with the power and simplicity of crewAI.
