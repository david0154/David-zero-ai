# ai_core/task_handler.py

import os
import time
import shutil

class TaskHandler:
    def __init__(self):
        self.output_dir = "generated_projects"

        # Create output folder if not exists
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

    def handle(self, task_description, models):
        print(f"\n🎯 Task Received: {task_description}")
        print("🧠 Using AI models to plan and generate code...")

        # Use the models to understand and break down the task
        full_project_code = self.generate_code(task_description, models)

        timestamp = int(time.time())
        project_path = os.path.join(self.output_dir, f"project_{timestamp}")
        os.makedirs(project_path, exist_ok=True)

        with open(os.path.join(project_path, "main.py"), "w", encoding="utf-8") as f:
            f.write(full_project_code)

        print(f"\n✅ Project generated at: {project_path}")
        print("📦 Ready to run and build!")
    
    def generate_code(self, task, models):
        # Combine multiple pretrained models' outputs
        print("⚙️ Thinking...")
        base_code = ""

        for model in models:
            suggestion = model.generate(task)
            base_code += f"\n\n# --- Model Output ({model.name}) ---\n"
            base_code += suggestion

        return base_code.strip()
