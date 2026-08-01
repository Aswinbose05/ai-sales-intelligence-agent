"""
Ollama LLM Client
"""

from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage

from src.config import (
    OLLAMA_MODEL,
    OLLAMA_URL,
    TEMPERATURE,
)


class OllamaClient:

    def __init__(self):

        self.llm = ChatOllama(
            model=OLLAMA_MODEL,
            base_url=OLLAMA_URL,
            temperature=TEMPERATURE,
        )

    def invoke(self, prompt: str) -> str:

        system_prompt = (
            "You are a JSON API.\n"
            "Return ONLY valid JSON.\n"
            "Do NOT explain.\n"
            "Do NOT use markdown.\n"
            "Do NOT say hello.\n"
            "Do NOT wrap the JSON inside ```.\n\n"
        )

        try:

            response = self.llm.invoke([
                HumanMessage(content=system_prompt + prompt)
            ])

            text = response.content.strip()

            # Remove markdown if the model still returns it
            text = text.replace("```json", "")
            text = text.replace("```", "")
            text = text.strip()

            return text

        except Exception as e:

            print("Ollama Error:", e)

            return "[]"


# Singleton
ollama_client = OllamaClient()


if __name__ == "__main__":

    prompt = """
Return exactly this JSON.

[
    {
        "name": "John"
    }
]
"""

    result = ollama_client.invoke(prompt)

    print(result)