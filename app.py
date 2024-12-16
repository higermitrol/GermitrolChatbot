import os
from flask import Flask, request, jsonify, send_from_directory
import openai

# Set your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

if not openai.api_key:
    raise ValueError("OPENAI_API_KEY environment variable is not set")

app = Flask(__name__)

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/chat', methods=['POST'])
def chat():
    try:
        user_message = request.json.get("message")
        if not user_message:
            return jsonify({"error": "Message is required"}), 400

        # Use the ChatCompletion API
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Use a chat model like gpt-3.5-turbo or gpt-4
            messages=[
                {"role": "system", "content": "You are a helpful assistant for a UV air purifier company."},
                {"role": "user", "content": user_message}
            ],
            max_tokens=150
        )

        reply = response['choices'][0]['message']['content'].strip()
        return jsonify({"reply": reply})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
