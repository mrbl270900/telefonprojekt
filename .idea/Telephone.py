from playsound import playsound
import sounddevice as sd
from scipy.io.wavfile import write
import os, os.path
import keyboard  # using module keyboard
import random
#import RPi.GPIO as GPIO

#setup of recording
fs = 44100  # Sample rate
seconds = 5  # Duration of recording
path = "C:/Users/mads/IdeaProjects/telefonprojekt/.idea/Lyd"
#path_tone_besked = "C:/Users/mads/IdeaProjects/telefonprojekt/.idea/lyd_her"

#TODO implementer dette på raspi
#brugt for at læse pin 4 af raspary pi og hvis den bliver trykket på giver den false eller true
#GPIO.setmode(GPIO.BOARD)
#GPIO.setup(18, GPIO.OUT)
#GPIO.setup(31, GPIO.IN)
#herunder læser vi vores input
#print GPIO.input(31)
#skriver high eller low til en pin som vores lys kontorler kan læse (arduino)
#GPIO.output(18, GPIO.HIGH)

#husk at ryde op når kode slutter
#GPIO.cleanup()


while(True):
        if keyboard.is_pressed('q'):  # if key 'q' is pressed her skal vi have i stedet for q have vores input

            #TODO tilføj noget vente tid her for tiden det tager at få telefonen op til øret
            #time.sleep(0.2)

            #TODO tilføj et signal til vores lys her
            #GPIO.output(18, GPIO.HIGH)
            #time.sleep(0.1)
            #GPIO.output(18, GPIO.LOW)

            #afspil tilfældig optaget lyd
            list = os.listdir(path)
            number_lyd = len(list)
            tilfoldigt_nr = random.randint(1,number_lyd-1)
            print(tilfoldigt_nr)

            playsound(path + "/lyd" + str(tilfoldigt_nr) + ".wav")

            #TODO tilføj en indspillet lyd her der forklare at de skal lægge en besked efter tonen
            #playsound(path_tone_besked)

            #optager
            myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
            print("optager")
            sd.wait()  # Wait until recording is finished

            #gemmer
            list = os.listdir(path) # dir is your directory path
            number_lyd = len(list)
            navn = "lyd" + str(number_lyd) + ".wav"
            write('Lyd/' + navn, fs, myrecording)  # Save as WAV file
            print("optager færdig")

            #TODO skal fjernes før færdig del da dette er en teste funktion
            playsound(path + '/lyd' + str(number_lyd) + '.wav')
            print("afspil færdig")