from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class ProjetoAnaliseMercado():
    """ProjetoAnaliseMercado crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def pesquisador_mercado(self) -> Agent:
        return Agent(
            config=self.agents_config['pesquisador_mercado'], # type: ignore[index]
            verbose=True
        )

    @agent
    def analista_tendencia(self) -> Agent:
        return Agent(
            config=self.agents_config['analista_tendencia'], # type: ignore[index]
            verbose=True
        )

    @agent 
    def redator(self) -> Agent: 
        return Agent( 
            config=self.agents_config['redator'], 
            verbose=True
        )
   
    @task
    def pesquisa_mercado(self) -> Task:
        return Task(
            config=self.tasks_config['pesquisa_mercado'], 
        ) 

    @task 
    def analise_mercado(self) -> Task: 
        return Task( 
            config=self.tasks_config['analise_mercado'],
        )

    @task 
    def relatorio(self) -> Task: 
        return Task( 
            config=self.tasks_config['relatorio'], 
            output_file='relatorio.html'
        )
    @crew
    def crew(self) -> Crew:
        """Creates the ProjetoAnaliseMercado crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
