import speech_recognition as sr
from talk import talk


# create a recognizer instance
r = sr.Recognizer()


# create a microphone instance
mic = sr.Microphone()

# adjust the recognizer sensitivity to ambient noise
r.energy_threshold = 300


def get_info():
    s = ""
    with mic as source:
        # adjust the microphone sensitivity to ambient noise
        r.adjust_for_ambient_noise(source)
        while True:
            # listen for speech
            print("Listening...")
            audio = r.listen(source)
            print('Ok!!')

            try:
                # recognize speech using Google Speech Recognition
                print("-->")
                text = r.recognize_google(audio).lower()
                print(f"You said: {text}")

                if text == "stop" or text == "top" or text == "Stop" or text == "op" or text == "stop stop stop stop" or text == "stop stop stop" or text == "stop stop":
                    print("one")
                    return s
                else:
                    print("two")
                    s += text
            except sr.UnknownValueError:
                print("Speech recognition could not understand audio")
                talk("Speech recognition could not understand audio")
                print("Please repeat again")
                talk("Please repeat again")
            except sr.RequestError as e:
                print(
                    f"Could not request results from Google Speech Recognition service; {e}")
                talk(
                    f"Could not request results from Google Speech Recognition service;{e}")
