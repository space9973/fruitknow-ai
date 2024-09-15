# schemas.py
from marshmallow import Schema, fields

class FAQSchema(Schema):
    id = fields.Int(dump_only=True)
    question = fields.Str(required=True)
    answer = fields.Str(required=True)

faq_schema = FAQSchema()
faqs_schema = FAQSchema(many=True)
