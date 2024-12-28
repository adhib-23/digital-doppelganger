from flask import Flask, request, jsonify, render_template
from model.personality import analyze_personality
from model.text_generator import generate_response

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    user_data = request.json['user_data']
    traits = analyze_personality(user_data)
    return jsonify(traits)

@app.route('/respond', methods=['POST'])
def respond():
    prompt = request.json['prompt']
    user_style = request.json['user_style']
    response = generate_response(prompt, user_style)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
