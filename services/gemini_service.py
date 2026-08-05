from groq import Groq
from core.config import settings

client = Groq(api_key=settings.GROQ_API_KEY)


def generate_questions(body):

    prompt = f"""
You are an expert technical interviewer.

Generate exactly {body.questionCount} interview questions.

Role: {body.role}

Experience: {body.experience}

Difficulty: {body.difficulty}

Interview Type: {body.interviewType}

Skills:
{", ".join(body.skills)}

Return ONLY valid JSON.

Example:

{{
  "questions": [
    {{
      "id": 1,
      "question": "Explain React Hooks."
    }},
    {{
      "id": 2,
      "question": "What is Virtual DOM?"
    }}
  ]
}}
"""

    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {
                "role": "system",
                "content": "You are an expert technical interviewer."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.7,
    )

    return response.choices[0].message.content