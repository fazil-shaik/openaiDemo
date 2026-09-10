import os

from openai import OpenAI

MODEL = "gpt-4o-mini"


def get_client():
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError(
            "Missing OPENAI_API_KEY. Export it first: export OPENAI_API_KEY='your_key_here'"
        )
    return OpenAI(api_key=api_key)


def generate_response(prompt, system_prompt="You are a helpful assistant.", temperature=0.7, max_tokens=120):
    client = get_client()
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt},
        ],
        temperature=temperature,
        max_tokens=max_tokens,
    )
    return response.choices[0].message.content.strip()


def compare_temperatures(prompt, system_prompt="You are a concise creative writing assistant."):
    print(f"\nPrompt: {prompt}")
    for temperature in (0.2, 0.7, 1.2):
        print(f"\n--- temperature={temperature} ---")
        result = generate_response(prompt, system_prompt=system_prompt, temperature=temperature, max_tokens=80)
        print(result)


if __name__ == "__main__":
    user_prompt = input("Enter a prompt: ").strip() or "Write a short poem about the ocean."
    system_prompt = "You are a creative and concise assistant."

    print("\nSingle response with default settings:")
    print(generate_response(user_prompt, system_prompt=system_prompt, temperature=0.7, max_tokens=80))

    print("\nComparing different temperature values:")
    compare_temperatures(user_prompt, system_prompt=system_prompt)