from transformers import BertTokenizer, BertModel
import torch

# Инициализация токенизатора и модели BERT
tokenizer = BertTokenizer.from_pretrained('bert-base-multilingual-cased')
model = BertModel.from_pretrained('bert-base-multilingual-cased')


def text_to_vector(text):
    """
    Преобразование текста в векторное представление с использованием модели BERT.

    Args:
        text (str): Текст для преобразования.

    Returns:
        list: Векторное представление текста.
    """
    encoded_input = tokenizer(text, return_tensors='pt', padding=True, truncation=True, max_length=128)
    with torch.no_grad():
        output = model(**encoded_input)
    embeddings = output.last_hidden_state.mean(1).squeeze().tolist()
    return embeddings


def analyze_text(text):
    """
    Функция для анализа текста и выявления ключевых особенностей.

    Args:
        text (str): Текст для анализа.

    Returns:
        dict: Словарь с анализом текста.
    """
    vector = text_to_vector(text)
    return {"vector": vector}


if __name__ == "__main__":
    sample_text = "Привет, как дела?"
    print(analyze_text(sample_text))
