from flask import request, jsonify
from voice_processing import handle_incoming_call, transcribe_audio
from text_processing import text_to_vector, decode_information
from response_generation import generate_response, send_response

def setup_routes(app):
    @app.route('/incoming_call', methods=['POST'])
    def incoming_call():
        return handle_incoming_call(request)

    @app.route('/process_audio', methods=['POST'])
    def process_audio():
        text = transcribe_audio(request.data)
        vector = text_to_vector(text)
        information = decode_information(vector)
        response = generate_response(information)
        send_response(response)
        return jsonify({"response": "Processed"}), 200
