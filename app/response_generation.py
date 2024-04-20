from gtts import gTTS
import os


def generate_response(information):
    """
    Генерация текстового ответа на основе анализа информации.

    Args:
        information (dict): Словарь с анализом текста, полученный из модулей NLP.

    Returns:
        str: Сгенерированный текстовый ответ.
    """
    # Пример простой генерации ответа
    response = "Вы сказали: " + information.get('text', 'ничего не понял')
    return response


def text_to_speech(text, lang='ru'):
    """
    Преобразование текста в аудиофайл используя Google Text-to-Speech.

    Args:
        text (str): Текст для преобразования в аудио.
        lang (str): Языковой код для генерации речи.

    Returns:
        str: Путь к аудиофайлу.
    """
    tts = gTTS(text=text, lang=lang)
    file_path = "output.mp3"
    tts.save(file_path)
    return file_path


def send_response(text, user_id, method='text'):
    """
    Отправка ответа пользователю через выбранный метод.

    Args:
        text (str): Текст ответа.
        user_id (str): Идентификатор пользователя.
        method (str): Метод отправки ('text' или 'voice').

    Returns:
        bool: Статус отправки ответа.
    """
    if method == 'voice':
        audio_path = text_to_speech(text)
        print(f"Voice response generated and sent to user {user_id} via {method}")
    else:
        print(f"Text response sent to user {user_id}: {text}")

    return True


if __name__ == "__main__":
    # Пример использования
    info = {'text': 'Привет, как дела?'}
    response_text = generate_response(info)
    send_response(response_text, 'user1234', 'text')
