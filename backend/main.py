from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS configuration to allow frontend interaction
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Static FAQs about fruits
fruit_faqs = [
    {
        "id": 1,
        "fruit": "Orange",
        "question": "What are the health benefits of eating oranges?",
        "answer": "Oranges are rich in Vitamin C, which boosts the immune system. They are also high in fiber, support heart health, and help in reducing inflammation."
    },
    {
        "id": 2,
        "fruit": "Kiwi",
        "question": "Why should I eat kiwis regularly?",
        "answer": "Kiwis are high in Vitamin C, improve digestion, and are great for heart health. They also contain antioxidants and help in boosting the immune system."
    },
    {
        "id": 3,
        "fruit": "Papaya",
        "question": "How does papaya benefit digestion?",
        "answer": "Papayas contain the enzyme papain, which aids digestion. They are also rich in fiber and antioxidants, which help reduce inflammation and promote a healthy gut."
    },
    {
        "id": 4,
        "fruit": "Guava",
        "question": "What nutrients are in guavas?",
        "answer": "Guavas are packed with Vitamin C, dietary fiber, and antioxidants. They support immune function, digestive health, and help regulate blood sugar levels."
    }
]

# Route to get FAQs
@app.get('/api/faqs')
def get_faqs():
    return fruit_faqs

# To run FastAPI app using uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
