# 🤖 David AI – Zero David

**Author:** David  
**Email:** davidk76011@gmail.com  
**Model Name:** Zero David  
**Framework:** [Arya](https://github.com/david0154/Arya)  
**License:** MIT (Open Source)

---

## 🧠 What Is David AI?

David AI is a powerful offline AI assistant designed to **understand your instructions (voice or text)** and generate full working **websites or desktop software** with beautiful UI, logos, and fully working code. It uses a **custom framework (Arya)**, built-in voice support, and 4 open-source coding models.

---

## 🔥 Features

- ✅ Build complete full-stack websites
- ✅ Create full Windows desktop software
- ✅ Works 100% offline (internet only for first model download)
- ✅ Uses 4 powerful open-source pretrained coding models
- ✅ Voice + text interface (offline speech)
- ✅ Beautiful UI generation with logos
- ✅ Custom AI training via Arya framework

---

## 💻 System Requirements

| Component       | Minimum              | Recommended              |
|----------------|----------------------|---------------------------|
| OS             | Windows 10 or 11     | Windows 11                |
| Python         | 3.10 or newer        | Latest version            |
| Memory (RAM)   | 16 GB                | 32 GB or more             |
| Disk Space     | 40 GB                | 80 GB+                    |
| GPU            | Optional (CUDA)      | 24GB VRAM for model speed |
| Tools Required | Git, VS Code         | Git, VS Code              |

---

## 📦 Pretrained AI Models Used

These are downloaded automatically the first time you run David AI.

| Model Name      | HuggingFace Path                        |
|------------------|-----------------------------------------|
| CodeLlama 7B     | `codellama/CodeLlama-7b-hf`             |
| StarCoder2 7B    | `bigcode/starcoder2-7b`                 |
| DeepSeek Coder   | `deepseek-ai/deepseek-coder-6.7b-base`  |
| WizardCoder 15B  | `WizardLM/WizardCoder-15B-V1.0`         |

---

## 🛠️ Installation Guide (Step-by-Step)

### 🔹 Step 1: Clone the Repository

```bash
git clone https://github.com/david0154/David-zero-ai
cd david_ai
```

### 🔹 Step 2: Create a Virtual Environment (Windows)

```bash
python -m venv venv
venv\Scripts\activate
```

### 🔹 Step 3: Install All Dependencies

```bash
pip install -r requirements.txt
```

---

## 🚀 First Run

```bash
python main.py
```

David AI will:
- Clone the Arya framework (if not present)
- Download pretrained AI coding models
- Launch the AI with voice + text interface
- Speak: **"What do you want me to build today?"**

---

## 💬 Example Commands

Here are some real prompts you can give to Zero David:

```txt
Build a Facebook-like website with login, posts, and chat.
Create a Windows desktop app to manage inventory and print reports.
Make a portfolio website in HTML/CSS/JS with contact form and animations.
Build an AI-powered chatbot in Python with GUI and SQLite database.
Generate a modern blog system using Django, PostgreSQL and TailwindCSS.
```

---

## 🧠 Training David AI

### ✅ Option 1 – Train from a `.txt` dataset

```python
from ai_core.training.trainer import DavidTrainer

trainer = DavidTrainer()
trainer.train_on_dataset("my_code.txt")
```

### ✅ Option 2 – Train from Your Codebase

```python
from ai_core.training.trainer import DavidTrainer

trainer = DavidTrainer()
trainer.train_with_arya("my_projects/")
```

---

## 🎙️ Voice Support (Offline)

David AI speaks responses using `pyttsx3`, fully offline.

If voice doesn’t work, install:

```bash
pip install pyttsx3 pypiwin32
```

---

## 📁 Project Structure

```
david_ai/
├── ai_core/
│   ├── zero_david.py        ← AI logic
│   ├── voice_module.py      ← Voice system
│   ├── task_handler.py      ← Project generator
│   └── training/
│       ├── trainer.py       ← Custom training support
│       └── models_config.py ← Model integration
├── arya_core/               ← Arya framework (auto-downloaded)
├── generated_projects/      ← All output
├── requirements.txt         ← Dependency list
├── main.py                  ← App entry point
└── README.md                ← You're here!
```

---

## 📜 requirements.txt

```txt
transformers
torch
pyttsx3
pypiwin32
datasets
requests
gitpython
```

---

## 🧪 Common Commands

| Task                              | Command                                                   |
|-----------------------------------|------------------------------------------------------------|
| 🟢 Start AI assistant              | `python main.py`                                           |
| 📦 Install all dependencies        | `pip install -r requirements.txt`                         |
| 🧠 Train on `.txt` dataset         | `trainer.train_on_dataset("my_code.txt")`                 |
| 📂 Train on code folder (Arya)     | `trainer.train_with_arya("my_projects/")`                 |
| 🎙️ Fix voice errors (Win32)       | `pip install pyttsx3 pypiwin32`                           |

---

## 🧯 Troubleshooting

| Issue                             | Solution                                                   |
|-----------------------------------|-------------------------------------------------------------|
| Voice not working                 | Install: `pip install pyttsx3 pypiwin32`                   |
| Arya not found                    | Auto-downloaded or manually clone into `/arya_core`        |
| Memory error with models          | Use lower model sizes or quantized versions                |
| No output in `generated_projects` | Check console logs for errors or simplify the prompt       |
| Models not downloading            | Check internet connection and HuggingFace availability     |

---

## 📬 Author Info

**👤 Name:** David  
**📧 Email:** davidk76011@gmail.com  
**🌐 GitHub:** [github.com/david0154](https://github.com/david0154)  
**🧠 AI Model:** Zero David  
**⚙️ Framework:** Arya

---

## ✅ You're All Set!

Just run:

```bash
python main.py
```

Then say or type something like:

```
Build me a task manager app with calendar, categories, and PDF export.
```

Zero David will:
- Understand
- Plan
- Build your app or website
- Deliver full code, design, and documentation

> 🎉 You now have your own offline AI software and website builder. Built with ❤️ by David using Arya Framework.

---
## ⚡ Also Available: David AI – Zero Light

Need to run David AI on a low-end PC or laptop?

👉 **[David AI – Zero Light (Low Resource Version)](https://github.com/david0154/David-zero-ai-light-/)**

**Features of Zero Light:**
- Fully offline AI for coding + UI design
- Works with only **8 GB RAM**, **8 GB VRAM**, and **80 GB disk**
- Uses compact pretrained coding models (CodeGen, StarCoder-mini, etc.)
- Understands text instructions to generate full projects
- Automatically builds structured, colorful UI with logo and layout
- Simple CLI interface with optional voice support

💻 Ideal for:
- Low-end desktops or laptops
- Quick local development without internet
- Portable AI development environment

🔧 Tech Stack:
- Python 3.10+
- Arya Framework (optional)
- Lightweight model setup
- One-task-at-a-time execution

###

## 📖 License

```
MIT License

Copyright (c) 2025 David

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell   
copies of the Software, and to permit persons to whom the Software is        
furnished to do so, subject to the following conditions:                     

The above copyright notice and this permission notice shall be included in   
all copies or substantial portions of the Software.                          

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR  
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,    
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE 
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER      
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING     
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER         
DEALINGS IN THE SOFTWARE.
```
