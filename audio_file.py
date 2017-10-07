import sounddevice as sd
import win32com.client as wincl
speak = wincl.Dispatch("SAPI.SpVoice")
import numpy as np
import scipy.io.wavfile as wav

fs=44100 #Best audio frequency
duration = 10  # seconds
myrecording = sd.rec(duration *fs , samplerate=fs, channels=2, dtype='float64')
print("Recording Audio")
sd.wait()
sd.play(myrecording,fs)
sd.wait()
print("Play Audio Complete")
