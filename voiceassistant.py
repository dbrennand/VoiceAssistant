try:
    from gtts import gTTS
    import speech_recognition as sr
    from subprocess import Popen
    from time import ctime
    import webbrowser
except ImportError as err:
    print(f"Import error: {err}")


class voice_assistant:

    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()

    def capture(self):
        try:
            with self.microphone as source:
                print("Ask me something")
                audio_data = self.recognizer.listen(source)
                resp = self.recognizer.recognize_google(audio_data)
                print(f"The assistant heard: {resp}")
                return resp
        except AttributeError as err:
            print(
                f"AttributeError occured: {err}: Ensure you have PyAudio 0.2.11 or later installed.")
        except sr.UnknownValueError:
            print("Google Speech Recognition couldn't understand audio.")
        except sr.RequestError as err:
            print(
                f"Could not request results from Google Speech Recognition service: {err}")

    def assistant_speak(self, resp):
        tts = gTTS(resp, lang="en", slow=False)
        tts.save("audio.mp3")
        Popen(["afplay", "audio.mp3"])

    def assistant_handle(self, voice_input):
        try:
            if (("search") in (voice_input)):
                data = voice_input.split("search")
                search_query = str(data[1])
                self.assistant_speak(f"Searching Google for {search_query}")
                webbrowser.open(
                    f"https://www.google.co.uk/search?q={search_query}")
            elif (("time") in (voice_input)):
                self.assistant_speak(f"The time is {ctime()}")
            else:
                self.assistant_speak("Sorry, I do not know that command.")
        except sr.UnknownValueError:
            self.assistant_speak("Sorry, I do not know that command.")


# Initalisation: Example usage.
a = voice_assistant()
voice_input = a.capture()
a.assistant_handle(voice_input)
