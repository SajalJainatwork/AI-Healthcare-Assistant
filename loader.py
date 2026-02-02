import os
from dotenv import load_dotenv

def load_prompt(prompt_name):
    load_dotenv()
    prompt_path = os.getenv("PROMPT_FILE_PATH")
    if not prompt_path or not os.path.exists(prompt_path):
        raise FileNotFoundError(f"Prompt file not found at: {prompt_path}")

    with open(prompt_path, "r", encoding="utf-8") as file:
        content = file.read()

    # Split and parse sections
    sections = content.split("--- ")
    prompts = {}

    for section in sections:
        if not section.strip():
            continue
        lines = section.split("\n", 1)
        if len(lines) < 2:
            continue
        key = lines[0].strip()
        value = lines[1].strip()
        prompts[key] = value

    if prompt_name not in prompts:
        raise ValueError(f"Prompt '{prompt_name}' not found in prompts.txt")

    return prompts[prompt_name]

