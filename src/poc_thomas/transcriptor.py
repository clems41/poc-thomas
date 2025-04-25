from datetime import datetime

import whisper

class Transcriptor:
    model = "turbo"

    def transcribe(self, file_path: str) -> str:
        start_time = datetime.now()
        model = whisper.load_model(self.model)
        result = model.transcribe(file_path, language="fr", verbose=True, fp16=False)
        end_time = datetime.now()
        duration = end_time - start_time
        print("Durée de la transcription : {} minutes {} secondes".format(duration.seconds // 60, duration.seconds % 60))
        return result["text"]