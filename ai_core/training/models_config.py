# ai_core/training/models_config.py

from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
import torch

class BaseCodingModel:
    def __init__(self, name, model_id):
        self.name = name
        self.model_id = model_id
        self.tokenizer = AutoTokenizer.from_pretrained(model_id)
        self.model = AutoModelForCausalLM.from_pretrained(
            model_id, 
            torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
            device_map="auto"
        )
        self.generator = pipeline("text-generation", model=self.model, tokenizer=self.tokenizer)

    def generate(self, prompt):
        outputs = self.generator(prompt, max_length=2048, do_sample=True, top_p=0.95, temperature=0.7)
        return outputs[0]['generated_text']


class ModelLoader:
    def __init__(self):
        self.model_configs = [
            {"name": "CodeLlama", "id": "codellama/CodeLlama-7b-hf"},
            {"name": "StarCoder2", "id": "bigcode/starcoder2-7b"},
            {"name": "DeepSeek", "id": "deepseek-ai/deepseek-coder-6.7b-base"},
            {"name": "WizardCoder", "id": "WizardLM/WizardCoder-15B-V1.0"}
        ]

    def load_models(self):
        print("📦 Loading pretrained coding models...")
        models = []
        for cfg in self.model_configs:
            print(f"⏳ Loading {cfg['name']}...")
            try:
                model = BaseCodingModel(cfg["name"], cfg["id"])
                models.append(model)
                print(f"✅ {cfg['name']} loaded.")
            except Exception as e:
                print(f"❌ Failed to load {cfg['name']}: {e}")
        return models
