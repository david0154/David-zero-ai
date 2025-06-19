# ai_core/training/trainer.py

import os
from arya import AryaTrainer  # Assumes Arya is cloned or pip-installed
from transformers import AutoTokenizer, AutoModelForCausalLM, TrainingArguments, Trainer, TextDataset, DataCollatorForLanguageModeling

class DavidTrainer:
    def __init__(self, model_id="codellama/CodeLlama-7b-hf"):
        print("⚙️ Initializing training environment...")
        self.tokenizer = AutoTokenizer.from_pretrained(model_id)
        self.model = AutoModelForCausalLM.from_pretrained(model_id)

    def train_on_dataset(self, dataset_path):
        print(f"📚 Loading dataset from: {dataset_path}")
        dataset = TextDataset(
            tokenizer=self.tokenizer,
            file_path=dataset_path,
            block_size=512
        )

        data_collator = DataCollatorForLanguageModeling(
            tokenizer=self.tokenizer, mlm=False
        )

        args = TrainingArguments(
            output_dir="./checkpoints/david",
            overwrite_output_dir=True,
            num_train_epochs=3,
            per_device_train_batch_size=1,
            save_steps=100,
            save_total_limit=1,
            logging_dir="./logs"
        )

        print("🧠 Starting training using Transformers Trainer...")
        trainer = Trainer(
            model=self.model,
            args=args,
            data_collator=data_collator,
            train_dataset=dataset
        )

        trainer.train()
        print("✅ Training complete! Model saved to ./checkpoints/david")

    def train_with_arya(self, custom_code_data_dir):
        print("🧠 Training using Arya framework...")
        trainer = AryaTrainer(
            data_dir=custom_code_data_dir,
            output_dir="./checkpoints/david_arya",
            model_id="codellama/CodeLlama-7b-hf"
        )
        trainer.run()
