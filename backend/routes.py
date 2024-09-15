# routes.py
from flask import Blueprint, request, jsonify
from models import db, FAQ
from schemas import faq_schema, faqs_schema

api = Blueprint('api', __name__)

# GET /faqs - Fetch all FAQs
@api.route('/faqs', methods=['GET'])
def get_faqs():
    faqs = FAQ.query.all()
    return faqs_schema.jsonify(faqs), 200

# GET /faqs/<id> - Fetch a single FAQ by ID
@api.route('/faqs/<int:id>', methods=['GET'])
def get_faq(id):
    faq = FAQ.query.get_or_404(id)
    return faq_schema.jsonify(faq), 200

# POST /faqs - Create a new FAQ
@api.route('/faqs', methods=['POST'])
def create_faq():
    data = request.get_json()
    faq = faq_schema.load(data)
    new_faq = FAQ(question=faq['question'], answer=faq['answer'])
    db.session.add(new_faq)
    db.session.commit()
    return faq_schema.jsonify(new_faq), 201

# PUT /faqs/<id> - Update a FAQ by ID
@api.route('/faqs/<int:id>', methods=['PUT'])
def update_faq(id):
    faq = FAQ.query.get_or_404(id)
    data = request.get_json()
    updated_data = faq_schema.load(data, partial=True)
    faq.question = updated_data.get('question', faq.question)
    faq.answer = updated_data.get('answer', faq.answer)
    db.session.commit()
    return faq_schema.jsonify(faq), 200

# DELETE /faqs/<id> - Delete a FAQ by ID
@api.route('/faqs/<int:id>', methods=['DELETE'])
def delete_faq(id):
    faq = FAQ.query.get_or_404(id)
    db.session.delete(faq)
    db.session.commit()
    return '', 204
