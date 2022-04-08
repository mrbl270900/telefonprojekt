from playsound import playsound
import sounddevice as sd
from scipy.io.wavfile import write
import os, os.path
import keyboard  # using module keyboard
import random

#setup of recording
fs = 44100  # Sample rate
seconds = 5  # Duration of recording


while(True):
    if keyboard.is_pressed('m'):  # if key 'q' is pressed
        myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
        print("optager")
        sd.wait()  # Wait until recording is finished

        #gemmer
        write('C:/Users/madsr/IdeaProjects/telephonetest/.idea/Lyd/info2.wav', fs, myrecording)  # Save as WAV file
        print("optager færdig")

    if keyboard.is_pressed('q'):  # if key 'q' is pressed
        #afspiller lyd vi har optaget til start inf
        playsound("C:/Users/madsr/IdeaProjects/telephonetest/.idea/Lyd/info1.wav")


        #afspil tilfældig optaget lyd
        list = os.listdir('C:/Users/madsr/IdeaProjects/telephonetest/.idea/Lyd')
        number_lyd = len(list)
        tilfoldigt_nr = random.randint(1,number_lyd-1)
        print(tilfoldigt_nr)

        playsound("C:/Users/madsr/IdeaProjects/telephonetest/.idea/Lyd/lyd" + str(tilfoldigt_nr) + ".wav")

        #afspiller lyd før optagelse
        playsound("C:/Users/madsr/IdeaProjects/telephonetest/.idea/Lyd/info2.wav")

        #optager
        myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
        playsound("C:/Users/madsr/IdeaProjects/telephonetest/.idea/Lyd/ding-sound-effect_2.mp3")
        print("optager")
        sd.wait()  # Wait until recording is finished

        #gemmer
        list = os.listdir('C:/Users/madsr/IdeaProjects/telephonetest/.idea/Lyd') # dir is your directory path
        number_lyd = len(list)
        navn = "lyd" + str(number_lyd) + ".wav"
        write('Lyd/' + navn, fs, myrecording)  # Save as WAV file
        print("optager færdig")
        playsound("C:/Users/madsr/IdeaProjects/telephonetest/.idea/Lyd/ding-sound-effect_2.mp3")

        #afspiller skal fjernes, anvends til test pt
        #playsound('C:/Users/madsr/IdeaProjects/telephonetest/.idea/Lyd/lyd' + str(number_lyd) + '.wav')
        #print("afspil færdig")
