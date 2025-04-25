from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List

# llm=LLM(model="cas/ministral-8b-instruct-2410_q4km", base_url="http://localhost:11434")
# llm=LLM(model="ollama/mistral", base_url="http://localhost:11434")
llm = LLM(
     model="mistral/mistral-large-latest",
     temperature=0
)
results_directory = "short_version/results/"

@CrewBase
class ShortVersionCrew():
	"""LatestAiDevelopment crew"""
	agents: List[BaseAgent]
	tasks: List[Task]

	def __init__(self, filename: str):
		self.filename = filename
		self.results_directory = results_directory
		super().__init__()

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
			output_file=results_directory + self.filename + "_transcription_improved.txt"
		)

	@task
	def transcription_to_tasks(self) -> Task:
		return Task(
			config=self.tasks_config['transcription_to_tasks'],
			output_file=results_directory + self.filename + "_final.json"
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