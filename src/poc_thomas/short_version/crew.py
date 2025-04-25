from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List

llm=LLM(model="ollama/mistral", base_url="http://localhost:11434")
"""
llm = LLM(
     model="mistral/mistral-large-latest",
     temperature=0.7
)
"""

@CrewBase
class ShortVersionCrew():
	"""LatestAiDevelopment crew"""
	agents: List[BaseAgent]
	tasks: List[Task]

	@agent
	def transcription_improver(self) -> Agent:
		return Agent(
			config=self.agents_config['transcription_improver'],
			verbose=True,
            llm=llm,
		)

	@agent
	def task_manager(self) -> Agent:
		return Agent(
			config=self.agents_config['task_manager'],
			verbose=True,
            llm=llm,
		)

	@task
	def transcription_improvement(self) -> Task:
		return Task(
			config=self.tasks_config['transcription_improvement'],
		)

	@task
	def transcription_to_tasks(self) -> Task:
		return Task(
			config=self.tasks_config['transcription_to_tasks'],
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the LatestAiDevelopment crew"""
		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
            name='Sebania Crew',
		)