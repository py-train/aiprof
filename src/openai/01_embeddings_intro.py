"""
01_embeddings_intro.py

Goal:
- Call an OpenAI embedding model.
- Convert a sentence into a vector of numbers.
- Help beginners see that AI eventually works with numbers.

Before running:
1. Install dependencies from requirements.txt
2. Set your API key as an environment variable:
   export OPENAI_API_KEY="your_key_here"
"""

import os
from openai import OpenAI


EMBEDDING_MODEL = "text-embedding-3-small"


def build_client():
    """Create and return an OpenAI client."""
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        raise ValueError(
            "OPENAI_API_KEY is not set. Please export it before running this script."
        )

    return OpenAI(api_key=api_key)


def get_embedding(client, text, model=EMBEDDING_MODEL):
    """Request an embedding vector for the given text."""
    response = client.embeddings.create(
        model=model,
        input=text,
        encoding_format="float",
    )
    return response.data[0].embedding


def main():
    """Run a small embedding demo."""
    client = build_client()

    text = "OpenAI embeddings turn text into numbers that capture meaning."
    embedding = get_embedding(client, text)

    print("Original text:")
    print(text)
    print()

    print("What is an embedding?")
    print("An embedding is a list of numbers that represents the meaning of text.")
    print("Nearby meanings often have numerically similar vectors.")
    print()

    print(f"Embedding length: {len(embedding)}")
    print("First 10 numbers from the embedding:")
    print(embedding[:10])
    print()

    print("Try this next:")
    print("- Change the sentence and run again.")
    print("- Compare two similar sentences and see that both become number lists.")
    print("- Print the first 20 values instead of 10.")


if __name__ == "__main__":
    main()
