from datetime import datetime

from poc_thomas.database import DatabaseManager
from poc_thomas.short_version.crew import ShortVersionCrew

def run():
    """
    Run the crew.
    """
    # CONFIG
    db_manager = DatabaseManager()
    cultures = db_manager.get_cultures()
    activites = db_manager.get_activites()

    # INPUT
    with open("transcriptions/maraicher2.txt", "r") as f:
        transcription = f.read()
    inputs = {
        'transcription': transcription,
        'cultures': str(cultures),
        'activites': str(activites)
    }

    # EXECUTION
    start_time = datetime.now()
    ShortVersionCrew().crew().kickoff(inputs=inputs)
    end_time = datetime.now()
    duration = end_time - start_time
    print("Durée de l'exécution : {} minutes {} secondes".format(duration.seconds // 60, duration.seconds % 60))
