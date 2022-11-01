import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import wikipedia
import pyaudio
import time
import os
import smtplib
from weather import weatherfunc
from databasecontrol import pull_password, is_user, pull_audio, print_database
import emailsend


# weather - DONE
# wikipedia - DONE
# shut down computer - TEST
# send an email/text -
# make to do list -
# do translation -
# determine connections to computer -
# calender functionality -
# turn on/off music -
# do math -
# convert timezone -


# current things that need to be fixed: disabling for audio and text, does weather work with text?

engine = pyttsx3.init()

r = sr.Recognizer()
mic = sr.Microphone()
print("Using default microphone input...")
for microphone in mic.list_microphone_names():
    if str(microphone) == "Megan’s AirPods":
        print("Airpods Found...")
        micin = mic.list_microphone_names().index(microphone)
        print("...")
        mic = sr.Microphone(device_index=micin)
        print("Using Airpods")
        break



def printt(text):
    engine.say(text)
    engine.runAndWait()


def any_audio():
    with mic as source:
        audio = r.listen(source)
    audio_to_text = r.recognize_google(audio)
    return audio_to_text


def scared_dan():
    print("You have entered incorrect data. I am now afraid of you and will be running away, screaming.")
    time.sleep(2)
    for i in range(1000):
        print("A")
    print("H")


def convert_timezone():
    pass


def find_wikipedia_audio(subject):
    result = wikipedia.search(subject, results=5)
    printt(result)
    printt("Which of these options do you want to search?")
    option = any_audio()
    inList = False
    for resul in result:
        if resul == option:
            inList = True
    if inList == True:
        printt(wikipedia.summary(option, sentences=2))
    else:
        printt(
            "That was not an option. Your request cannot be completed at this time. Come back later to see if there is a wikipedia page on your desired topic.")


def find_wikipedia_text(subject):
    result = wikipedia.search(subject, results=5)
    print(result)
    print("Which of these options do you want to search?")
    option = input("")
    inListt = False
    for resul in result:
        if resul == option:
            inListt = True
    if inListt == True:
        print(wikipedia.summary(option, sentences=3))
        time.sleep(3)
        option = option.replace(" ", "_")
        webbrowser.open("https://en.wikipedia.org/wiki/" + option)
    else:
        print(
            "That was not an option. Your request cannot be completed at this time. Come back later to see if there is a wikipedia page on your desired topic.")


def welcome():
    print_database()
    print("Welcome. I am DAN. Which user is currently active?")
    user = input("")
    right_pass = ""
    user_found = is_user(user)
    if user_found == True:
        passin = input("Hello, " + user + "! Please enter your password. ")
        if passin == pull_password(user):
            print("You're in!")
            print("Using default Audio Preference...")
            change = input(
                "Click the C button if you want to temporarily change your audio preference! Press Enter if not.")
            if change == "C":
                print("Please enter Audio Mode to continue:")
                audio_mode = input("")
                if audio_mode.upper() == "TRUE":
                    get_audio_request()
                elif audio_mode.upper() == "FALSE":
                    get_text_request()
            else:
                preference = pull_audio(user)
                if preference == 0:
                    get_text_request()
                elif preference == 1:
                    get_audio_request()
        else:
            scared_dan()
    elif user_found == False:
        scared_dan()


def disable_audio():
    time.sleep(60)
    printt("Would you like to end the session?")
    session_end = any_audio()
    if session_end.upper() == "TRUE" or session_end.upper() == "YES":
        printt("Goodbye!")

    else:
        get_audio_request()


def disable_text():
    time.sleep(60)
    print("Would you like to end the session?")
    session_end = input("")
    if session_end.upper() == "TRUE" or session_end.upper() == "YES":
        print("Goodbye!")

    else:
        get_text_request()


def get_audio_request():
    continueit = 0
    printt("I am Dan, your Desktop Assistant Naturalization. How can I assist you?")
    while continueit == 0:
        printt("Speak now ...")
        request = any_audio()
        printt(request)
        printt("Is this what you said?")
        correct = any_audio()
        for word in correct.split(" "):
            if word == "true" or word == "yes" or word == "affirmative" or word == "correct":
                printt("Processing your request.")
                for word in request.split(" "):
                    if word == "quit":
                        continueit = 1
                        printt("disabling....")
                        disable_audio()
                        quit
                    elif word == "weather":
                        printt("What is the desired location?")
                        location_to_text = any_audio()
                        printt(weatherfunc(location_to_text))
                        break
                    elif word == "wikipedia" or word == "wiki" or word == "information":
                        printt("What is the desired subject?")
                        subject_to_text = any_audio()
                        find_wikipedia_audio(subject_to_text)
                        break
                    elif word == "email" or word == "gmail" or word == "mail":
                        printt("What is the first part of your gmail account? ")
                        continue2 = any_audio()
                        address == continue2 + "@gmail.com"



        else:
            pass


def get_text_request():
    continueit = 0
    print("I am Dan, your Desktop Assistant Naturalization.")
    while continueit == 0:
        print("How can I assist you?")
        request = input("")
        print("Processing your request.")
        for word in request.split(" "):
            if word == "quit":
                continueit = 1
                print("disabling....")
                disable_text()
                quit
            elif word == "weather":
                print("What is the desired location?")
                location_to_text = input()
                print(weatherfunc(location_to_text))
                break
            elif word == "wikipedia" or word == "wiki" or word == "information":
                print("What is the desired subject?")
                subject_to_text = input("")
                find_wikipedia_text(subject_to_text)
                break
            elif word == "email" or word == "gmail" or word == "mail":
                print("What is the first part of your gmail account? ")
                continue2 = input("")
                address = continue2 + "@gmail.com"



if __name__ == '__main__':
    welcome()