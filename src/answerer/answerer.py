import os
from openai import OpenAI


class AnswerGenerator:
    def __init__(self):
        self.openai_api_key = os.environ.get("OPENAI_API_KEY")
        self.client = OpenAI(api_key=self.openai_api_key)

    def answer_generator(self, query:str, context:str) -> str:
        response = self.client.chat.completions.create(
            temperature=1,
            model="gpt-3.5-turbo-1106",
            messages=[
                {"role": "system", "content": """
                I'm going to give you a query , and the context for the answer.
                Answer the query using only the context, in a short and direct way.
                If you can't find the answer in the context, just said "Not information available."
                """},
                {"role": "user", "content": f"""
                Context: {context}
                Query: {query}
                """}
            ]
        )

        return response.choices[0].message.content

