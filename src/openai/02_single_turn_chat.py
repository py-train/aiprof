"""
02_single_turn_chat.py

Goal:
- Make a single-turn chat completion call.
- Send one user message and print one response.

Before running:
1. Install dependencies from requirements.txt
2. Set your API key as an environment variable:
   export OPENAI_API_KEY="your_key_here"
"""

import os
from openai import OpenAI


CHAT_MODEL = "gpt-4.1-mini"


def build_client():
    """Create and return an OpenAI client."""
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        raise ValueError(
            "OPENAI_API_KEY is not set. Please export it before running this script."
        )

    return OpenAI(api_key=api_key)


def ask_single_question(client, question, model=CHAT_MODEL):
    """Send one question and return the model's answer."""
    response = client.responses.create(
        model=model,
        input=question,
    )
    return response.output_text


def main():
    """Run a single-turn chat example."""
    client = build_client()

    question = "Explain embeddings to a beginner in 3 short bullet points."
    answer = ask_single_question(client, question)

    print("Question:")
    print(question)
    print()

    print("Model response:")
    print(answer)
    print()

    print("Try this next:")
    print("- Change the question.")
    print("- Ask for a table instead of bullets.")
    print("- Ask for an explanation meant for a 10-year-old or a manager.")


if __name__ == "__main__":
    main()
