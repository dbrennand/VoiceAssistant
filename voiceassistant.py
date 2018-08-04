try:
    from gtts import gTTS
    import speech_recognition as sr
    from subprocess import Popen
    from time import ctime
    import webbrowser
    from requests import post, get
    from base64 import b64encode
except ImportError as err:
    print(f"Import Error: {err}")


class voice_assistant:

    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        self.client_id = "Insert Your Key Here."
        self.client_secret = "Insert Your Key Here."

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

    def duck_search(self, voice_input):
        data = voice_input.split("search")
        search_query = str(data[1])
        self.assistant_speak(f"Searching DuckDuckgo for {search_query}")
        webbrowser.open(
            f"https://duckduckgo.com/?q={search_query}")

    def spotify_auth(self, client_id, client_secret):
        joined_str = f"{client_id}:{client_secret}"
        # Encode joined_str into bytes.
        byte_str = str.encode(joined_str, encoding='utf_8')
        # Encode byte_str to base64 byte string.
        base64string = b64encode(byte_str)
        # Decode base64string to normal base64 string (non-byte).
        base64decode = base64string.decode()
        # Add to headers dict for POST.
        headers = {"Authorization": f"Basic {base64decode}"}
        # Api token endpoint.
        endpoint = "https://accounts.spotify.com/api/token"
        # Body as required by spotify web api.
        # See: https://developer.spotify.com/documentation/general/guides/authorization-guide/
        body = {"grant_type": "client_credentials"}
        resp = post(endpoint, data=body, headers=headers)
        return resp.json()

    def get_track(self, json_resp, voice_input):
        # Replace "play" with "" and split on "by"
        track_artist = voice_input.replace("play", "").split("by")
        # Remove leading and trailing " "
        track_artist = [item.strip(" ") for item in track_artist]
        # If a space found for track or artist str's (in track_artist), replace with a "+".
        # Required by Spotify API.
        track_artist_url = [item.replace(" ", "+") for item in track_artist]
        # Pass track_artist[0]: Track name, track_artist[1]: Artist name as endpoint request.
        endpoint = f"https://api.spotify.com/v1/search?q=track:{track_artist_url[0]}+artist:{track_artist_url[1]}&type=track&market=GB&limit=1"
        token = json_resp["access_token"]
        headers = {"Authorization": f"Bearer {token}"}
        resp = get(endpoint, headers=headers).json()
        for item, track in enumerate(resp["tracks"]["items"]):
            # Gets track url from spotify dict returned.
            url = track["external_urls"]["spotify"]
            self.assistant_speak(f"Playing {track_artist[0]} by {track_artist[1]}")
            webbrowser.open(url)

    def assistant_handle(self, voice_input):
        try:
            if (("search") in (voice_input)):
                self.duck_search(voice_input)
            elif (("time") in (voice_input)) or (("date") in (voice_input)):
                self.assistant_speak(f"The time and date is {ctime()}")
            elif (("play") in (voice_input)):
                self.get_track(self.spotify_auth(
                    self.client_id, self.client_secret), voice_input)
            else:
                self.assistant_speak("Sorry, I do not know that command.")
        except TypeError:
            self.assistant_speak("Sorry, I didn't understand.")


# Initalisation: Example usage.
a = voice_assistant()
voice_input = a.capture()
a.assistant_handle(voice_input)
