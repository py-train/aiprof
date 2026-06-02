"""
03_multi_turn_chat.py

Goal:
- Support a multi-turn conversation without frameworks.
- Store conversation history in a simple Python list.
- Send the full history on each API call so the model keeps context.

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


def get_assistant_reply(client, conversation, model=CHAT_MODEL):
    """Send the conversation history and return the next assistant reply."""
    response = client.responses.create(
        model=model,
        input=conversation,
    )
    return response.output_text


def main():
    """Run a simple multi-turn chat loop."""
    client = build_client()

    # The conversation starts with a system-style instruction.
    # This helps guide the assistant's behavior.
    conversation = [
        {
            "role": "system",
            "content": "You are a patient AI tutor. Keep answers simple and beginner-friendly.",
        }
    ]

    print("Multi-turn chat demo")
    print("Type 'exit' to stop.\n")

    while True:
        user_message = input("You: ")

        if user_message.lower() == "exit":
            print("Goodbye!")
            break

        # Add the user's new message to the history.
        conversation.append({"role": "user", "content": user_message})

        assistant_reply = get_assistant_reply(client, conversation)
        print("Assistant:", assistant_reply)
        print()

        # Add the assistant reply too.
        # On the next turn, the full conversation will be sent again.
        conversation.append({"role": "assistant", "content": assistant_reply})


if __name__ == "__main__":
    main()
