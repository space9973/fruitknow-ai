from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow CORS for frontend requests

# Static FAQs with benefits of each fruit
fruit_faqs = [
    {
        "id": 1,
        "fruit": "Orange",
        "question": "What are the health benefits of eating oranges?",
        "answer": "Oranges are rich in Vitamin C, which boosts the immune system.",
        "benefits": [
            "Boosts immune system with high Vitamin C",
            "Rich in antioxidants that fight free radicals",
            "Supports heart health by lowering cholesterol",
            "Helps improve skin health"
        ],
        "image": "/images/orange.jpg"
    },
    {
        "id": 2,
        "fruit": "Kiwi",
        "question": "What are the benefits of eating kiwis?",
        "answer": "Kiwis are an excellent source of Vitamin C.",
        "benefits": [
            "Rich in Vitamin C and E",
            "Improves digestion with natural enzymes",
            "Helps boost immunity",
            "Supports heart health with potassium"
        ],
        "image": "/images/kiwi.jpg"
    },
    {
        "id": 3,
        "fruit": "Papaya",
        "question": "What are the benefits of eating papayas?",
        "answer": "Papayas contain papain, which helps with digestion.",
        "benefits": [
            "Rich in digestive enzymes",
            "Helps reduce inflammation",
            "Promotes a healthy digestive system",
            "Improves skin with Vitamin A"
        ],
        "image": "/images/papaya.jpg"
    },
    {
        "id": 4,
        "fruit": "Guava",
        "question": "What are the benefits of eating guavas?",
        "answer": "Guavas are high in Vitamin C and fiber.",
        "benefits": [
            "Boosts immune system with Vitamin C",
            "Supports heart health with potassium",
            "Improves digestion with dietary fiber",
            "Helps with weight loss"
        ],
        "image": "/images/guava.jpg"
    }
]

# Route to get FAQs
@app.route('/api/faqs', methods=['GET'])
def get_faqs():
    return jsonify(fruit_faqs)

if __name__ == "__main__":
    app.run(debug=True)
