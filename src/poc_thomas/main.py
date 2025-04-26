from datetime import datetime

from poc_thomas.database import DatabaseManager
from poc_thomas.short_version.crew import ShortVersionCrew
from poc_thomas.transcriptor import Transcriptor

def run_crew(filename: str):
    print("----------------------------   {}    ----------------------------".format(filename))
    crew = ShortVersionCrew(filename=filename)
    # CONFIG
    db_manager = DatabaseManager()
    cultures = db_manager.get_cultures()
    activites = db_manager.get_activites()
    unites = db_manager.get_unites()

    # TRANSCRIPTION
    transcriptor = Transcriptor()
    transcription = transcriptor.transcribe("../../files/" + filename + ".mp3")
    with open(crew.results_directory + filename + "_transcription.txt", "w") as text_file:
        text_file.write(transcription)

    # INPUT
    inputs = {
        'transcription': transcription,
        'cultures': str(cultures),
        'activites': str(activites),
        'unites': str(unites),
        "filename": filename
    }

    # EXECUTION
    start_time = datetime.now()
    crew.crew().kickoff(inputs=inputs)
    end_time = datetime.now()
    duration = end_time - start_time
    print("Durée de l'exécution : {} minutes {} secondes".format(duration.seconds // 60, duration.seconds % 60))
    print("--------------------------------------------------------")

def main():
    """
    Run the crew.
    """
    filenames = [
        "maraicher2",
        "250324Baptiste",
        "250324Clara",
        "250325OlivierBenhamou",
        "250326Baptiste1",
        "250326virginie"
    ]
    for filename in filenames:
        run_crew(filename)

if __name__ == '__main__':
    main()
