import os
import wave

import pyaudio

CHUNK = 1024

AUDIO_PATH = os.path.dirname(__file__)
COMPLETED_PATH = os.path.join(AUDIO_PATH, "completed.wav")
START_PATH = os.path.join(AUDIO_PATH, "start.wav")

class Audio:
    def __init__(self) -> None:
        self.p = pyaudio.PyAudio()

    def __del__(self):
        self.p.terminate()

    def play_audio(self, path: str):
        with wave.open(path, 'rb') as wf:
            stream = self.p.open(format=self.p.get_format_from_width(wf.getsampwidth()),
                            channels=wf.getnchannels(),
                            rate=wf.getframerate(),
                            output=True)

            while len(data := wf.readframes(CHUNK)):
                stream.write(data)

            stream.close()
