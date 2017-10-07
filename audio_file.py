import sounddevice as sd
import win32com.client as wincl
speak = wincl.Dispatch("SAPI.SpVoice")
import numpy as np
import scipy.io.wavfile as wav

fs=44100 #Best audio frequency
duration = 10  # this is a time slot
myrecording = sd.rec(duration *fs , samplerate=fs, channels=2, dtype='float64') # this are the values that are given to the recorder which is present in the sounddevice file.
print("Recording Audio")
sd.wait() # wait to sync
sd.play(myrecording,fs) 
# play your recorded audio
sd.wait()  # again wait to sync
print("Play Audio Complete")
