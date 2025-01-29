from flask import Flask, request, jsonify
from deepseek import DeepSeekClient  # Import DeepSeek AI SDK

app = Flask(__name__)

# Initialize DeepSeek AI client
deepseek_client = DeepSeekClient(api_key="your_deepseek_api_key")

@app.route("/chat", methods=["POST"])
def chat():
    # Get user input from the request
    user_input = request.json.get("message")

    # Send the input to DeepSeek AI for processing
    response = deepseek_client.generate_response(user_input)

    # Return the chatbot's response
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
