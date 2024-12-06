
import wave
import sys
import json
from typing import List

from vosk import Model, KaldiRecognizer, SetLogLevel

# You can set log level to -1 to disable debug messages
SetLogLevel(0)

class Vosk():
    def __init__(self, model:str='en-us', audio_path:str='./test.wav'):
        self._audio_path = audio_path
        self._model = Model(lang=model)
        self._wf = self._load_audio()
        
    def _load_audio(self): 
        wf = wave.open(sys.argv[1], "rb")
        if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getcomptype() != "NONE":
            print("Audio file must be WAV format mono PCM.")
            sys.exit(1)
        return wf
    
    def parse(wf) -> List[str]:
        rec = KaldiRecognizer(elf._model, wf.getframerate())
        rec.SetWords(True)
        rec.SetPartialWords(True)
        final_result = []
        while True:
            data = wf.readframes(4000)
            if len(data) == 0:
                break
            if rec.AcceptWaveform(data):
                r = json.loads(rec.Result())
                print(r['text'])
                final_result.append(r['text'])
            else:
                continue
        result = rec.FinalResult()
        f = json.loads(result)
        print(f['text'])
        final_result.append(f['text'])
        print(f'result = {final_result}')
        return final_result