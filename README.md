# OpenAI Check

A small Python project that demonstrates how to call the OpenAI Chat Completions API using `client.chat.completions.create()` and experiment with parameters such as `temperature`, `max_tokens`, and the `system` message.

## Prerequisites

- Python 3.12+
- An OpenAI API key

## Setup

1. Open a terminal in the project folder:

   ```bash
   cd /yourlocationProject
   ```

2. Create and activate a virtual environment:

   ```bash
   python3 -m venv myenv
   source myenv/bin/activate
   ```

3. Install dependencies:

   ```bash
   pip install -U pip
   pip install openai
   ```

4. Set your API key:

   ```bash
   export OPENAI_API_KEY="your_api_key_here" or Store in .env
   ```

## Run the script

```bash
python main.py
```

When prompted, enter a topic or prompt such as:

```text
Write a short poem about the moon.
```

## What the script demonstrates

- `temperature`: controls randomness in the response
- `max_tokens`: limits the length of the generated output
- `system` message: defines the assistant's role and behaviour
- comparing outputs at different temperature values

## Example output

The app will print:

- a single response at a default temperature
- a comparison of responses at `temperature=0.2`, `0.7`, and `1.2`

You can edit the prompt or system message directly in `main.py` to experiment with different behaviors.
