import os
from datetime import datetime

import whisper

class Transcriptor:
    model = "turbo"

    def __init__(self, model_path):
        self.model_path = model_path

    def transcribe(self, file_path: str) -> str:
        model = whisper.load_model(self.model, download_root=self.model_path)
        start_time = datetime.now()
        result = model.transcribe(file_path, language="fr", verbose=True, fp16=False)
        end_time = datetime.now()
        duration = end_time - start_time
        print("Durée de la transcription : {} minutes {} secondes".format(duration.seconds // 60, duration.seconds % 60))
        return result["text"]