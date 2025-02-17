#Recognizing speech requires audio input, and SpeechRecognition makes retrieving this input really easy.
#Instead of having to build scripts for accessing microphones and processing audio files from scratch,
#SpeechRecognition will have you up and running in just a few minutes.
import speech_recognition as sr
#initialize recognizer to recognize the audio
r = sr.Recognizer()
lang = "en-US"
def speak_and_recognize():
    #initialize source as sr.Microphone
    with sr.Microphone() as source:
        print("I am listening: ")
        #listen to the source and save it to audio
        audio = r.listen(source)
        try:
            #convert audio into text
            text = r.recognize_google(audio, language=lang)
            print("You said: {}".format(text))
        except:
            print("Sorry, I could not recognize your voice")


def choose_lang(name): 
    global lang
    if name == "english":
        lang = "en-US"
    elif name == "lithuanian":
        lang = "lt-LT"
    elif name == "russian":
        lang = "ru-RU"
    elif name == "spanish":
        lang = "es-ES"
    else:
        print("I could not recognize the selected language.")
    
option = ""
while option != "0":
    print("1. Recognize the speech")
    print("2. Choose a language for speech recognition")
    print("0. Exit")
    option = input("Option: ")

    if option == "1":
        speak_and_recognize()
    elif option == "2":
        name = input("Enter language: ")
        choose_lang(name)
    elif option == "0":
        print("The program has been closed successfully")
    else:
        print("You have selected and option i can not process")



