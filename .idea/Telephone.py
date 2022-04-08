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
        write('C:/Users/madsr/IdeaProjects/telephonetest/.idea/Lyd/info1.wav', fs, myrecording)  # Save as WAV file
        print("optager færdig")

    if keyboard.is_pressed('q'):  # if key 'q' is pressed
        #afspiller lyd vi har optaget til start info
        playsound("C://Users//madsr//IdeaProjects//telephonetest//.idea//Lyd//info1.wav")


        #afspil tilfældig optaget lyd
        list = os.listdir('C:/Users/madsr/IdeaProjects/telephonetest/.idea/Lyd')
        number_lyd = len(list)
        tilfoldigt_nr = random.randint(1,number_lyd-3)
        print(tilfoldigt_nr)

        playsound("C:/Users/madsr/IdeaProjects/telephonetest/.idea/Lyd/lyd" + str(tilfoldigt_nr) + ".wav")

        #afspiller lyd før optagelse
        playsound("C://Users//madsr//IdeaProjects//telephonetest//.idea//Lyd//info2.wav")

        #optager
        playsound("C:/Users/madsr/IdeaProjects/telephonetest/.idea/Lyd/Answering_machine_beep.wav")
        myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
        print("optager")
        sd.wait()  # Wait until recording is finished
        playsound("C:/Users/madsr/IdeaProjects/telephonetest/.idea/Lyd/Answering_machine_beep.wav")

        #gemmer
        list = os.listdir('C://Users//madsr//IdeaProjects//telephonetest//.idea//Lyd') # dir is your directory path
        number_lyd = len(list)-2
        navn = "lyd" + str(number_lyd) + ".wav"
        write('Lyd/' + navn, fs, myrecording)  # Save as WAV file
        print("optager færdig")

        #afspiller skal fjernes, anvends til test pt
        #playsound('C:/Users/madsr/IdeaProjects/telephonetest/.idea/Lyd/lyd' + str(number_lyd) + '.wav')
        #print("afspil færdig")
