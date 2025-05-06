import os

import yaml
from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List

# llm=LLM(model="cas/ministral-8b-instruct-2410_q4km", base_url="http://localhost:11434")
# llm=LLM(model="ollama/mistral", base_url="http://localhost:11434")
llm = LLM(
     model="mistral/mistral-small-latest",
     temperature=0.2
)

@CrewBase
class ShortVersionCrew:
	"""LatestAiDevelopment crew"""
	agents: List[BaseAgent]
	tasks: List[Task]

	def __init__(self, filename: str, output_directory: str):
		self.filename = filename
		self.output_directory = output_directory
		self.final_file_path = None
		super().__init__()

	@agent
	def thomas(self) -> Agent:
		return Agent(
			config=self.agents_config['thomas'],
			verbose=True,
            llm=llm,
		)

	@task
	def analyse_transcription(self) -> Task:
		output_file = os.path.join(self.output_directory, self.filename + "_final.json")
		self.final_file_path = output_file
		return Task(
			config=self.tasks_config['analyse_transcription'],
			output_file="/" + output_file
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