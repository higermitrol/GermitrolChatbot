from flask import Flask, request, jsonify
import openai

# Set your OpenAI API key
openai.api_key = "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"

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get("message")
    if not user_message:
        return jsonify({"error": "Message is required"}), 400

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant for a UV air purifier company."},
            {"role": "user", "content": user_message}
        ]
    )

    reply = response["choices"][0]["message"]["content"]
    return jsonify({"reply": reply})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
