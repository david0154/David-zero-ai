# ai_core/voice_module.py

import pyttsx3

class VoiceModule:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 175)  # Speech speed
        self.engine.setProperty('volume', 1.0)  # Volume level

    def speak(self, text):
        print(f"🗣️ {text}")
        self.engine.say(text)
        self.engine.runAndWait()
