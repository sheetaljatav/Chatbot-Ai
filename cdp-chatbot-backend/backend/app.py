from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/ask', methods=['POST'])
def ask_question():
    if not request.is_json:
        return jsonify({"error": "Unsupported Media Type. Please send JSON data."}), 415

    data = request.get_json()
    if not data or 'question' not in data:
        return jsonify({"error": "Invalid input. Please provide a 'question' in the JSON body."}), 400

    question = data['question'].lower()

    # Basic answers for each CDP
    if "segment" in question:
        return jsonify({"answer": "Visit https://segment.com/docs/ for detailed information on Segment."})
    elif "mparticle" in question:
        return jsonify({"answer": "Visit https://docs.mparticle.com/ for guidance on mParticle."})
    elif "lytics" in question:
        return jsonify({"answer": "Visit https://docs.lytics.com/ for details on Lytics."})
    elif "zeotap" in question:
        return jsonify({"answer": "Visit https://docs.zeotap.com/home/en-us/ for help with Zeotap."})
    # Advanced comparisons
    elif "compare" in question:
        return jsonify({
            "answer": (
                "Segment focuses on collecting and routing customer data, "
                "mParticle excels in real-time data streaming and integrations, "
                "Lytics specializes in building customer segments, "
                "and Zeotap emphasizes data privacy and compliance for marketing."
            )
        })
    # Default response for unrecognized questions
    else:
        return jsonify({"answer": "Sorry, I don't have an answer for that."})

if __name__ == '__main__':
    app.run(debug=True)
