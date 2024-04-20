# models/load_model.py
from transformers import AutoModel, AutoTokenizer

def load_pretrained_model(model_name):
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModel.from_pretrained(model_name)
    model.save_pretrained(f"./models/{model_name}")
    tokenizer.save_pretrained(f"./models/{model_name}")

if __name__ == "__main__":
    model_name = "bert-base-multilingual-cased"  # Пример названия модели
    load_pretrained_model(model_name)
