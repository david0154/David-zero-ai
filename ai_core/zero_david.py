# ai_core/zero_david.py

import os
import json
from ai_core.task_handler import TaskHandler
from ai_core.voice_module import VoiceModule
from ai_core.training.models_config import ModelLoader

class ZeroDavid:
    def __init__(self):
        self.voice = VoiceModule()
        self.task_handler = TaskHandler()
        self.models = ModelLoader().load_models()
        self.greet()

    def greet(self):
        print("✅ Zero David is initialized and ready.")
        self.voice.speak("Hello David. Zero David is ready for your task.")

    def run(self):
        while True:
            try:
                task = input("\n🧠 What do you want me to build today?\n> ")
                if task.lower() in ['exit', 'quit']:
                    self.voice.speak("Shutting down. Goodbye!")
                    break

                self.voice.speak("Analyzing your request...")
                self.task_handler.handle(task, self.models)

            except Exception as e:
                print(f"[ERROR] {e}")
                self.voice.speak("An error occurred while processing your task.")
