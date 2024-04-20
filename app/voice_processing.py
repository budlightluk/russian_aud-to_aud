from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor
import soundfile as sf

processor = Wav2Vec2Processor.from_pretrained("facebook/wav2vec2-large-xlsr-53-russian")
model = Wav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-large-xlsr-53-russian")

def transcribe_audio(audio_file_path):
    """
    Функция для транскрибации аудиофайла в текст.
    Параметры:
    audio_file_path : str
        Путь к аудиофайлу

    Возвращает:
    transcription : str
        Транскрибированный текст аудиофайла
    """
    speech, sample_rate = sf.read(audio_file_path)

    input_features = processor(speech, sampling_rate=sample_rate, return_tensors="pt", padding=True)

    with torch.no_grad():
        logits = model(input_features.input_values).logits

    predicted_ids = torch.argmax(logits, dim=-1)
    transcription = processor.batch_decode(predicted_ids)

    return transcription[0]

if __name__ == "__main__":
    audio_path = "path/to/your/audio/file.wav"
    print(transcribe_audio(audio_path))
