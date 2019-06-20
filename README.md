# VoiceAssistant
A Simple voice assistant.

## Current Features

* Search the web:
    Example: "Search what is the tallest building in the world"
* Tell you the time and date:
    Example: "What is the time?" or "What is the date?"
* Search for a track from spotify:
    Example: "Play Best Life by Hardy Caprio"
* Search Google Maps for a location:
    Example: "locate London Eye"

## Dependancies
[voiceassistant.py](voiceassistant.py) is written in python 3 so its **REQUIRED**

It requires the following packages:

1. gTTs
2. speech_recognition
3. PyAudio
4. Requests

Install dependancy for PyAudio using:
```
brew install portaudio
```

Install Python dependancies using the command:
```
pipenv install
```

* Tested on MacOS.

## Prerequisites
To use the search track feature you must:

  1. Have a **Spotify** Account.

  2. Go to Spotify's developer website and [create an application](https://beta.developer.spotify.com/dashboard/login).

  3. Navigate to you're apps dashboard and copy the Client ID and Client Secret.

  4. Place **Client ID**, **Client Secret** in the respective variables found in [voiceassistant](voiceassistant.py):
      ```
      self.client_id = "Insert Your Key Here."
      self.client_secret = "Insert Your Key Here."
      ```

## Download Options -- Installing

Extract and navigate to the zipfile directory and run voiceassistant by executing the main entry point file [voiceassistant.py](voiceassistant.py):
  ```
  python3 voiceassistant.py
  ```

## Authors -- Contributors

* **Dextroz** - *Author* - [Dextroz](https://github.com/Dextroz)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) for details.
