# scripts/modify_logic.py

import openai
import json
from pathlib import Path

def inject_contradiction(dialogue, turn_index):
    prompt = f"""
    Given this dialogue:
    {dialogue}

    Modify turn {turn_index} to contradict the user's earlier statement.
    """
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )
    return response['choices'][0]['message']['content']

if __name__ == "__main__":
    input_file = Path("data/dialogstudio_raw/sample.json")
    with input_file.open() as f:
        dialogue = json.load(f)

    modified = inject_contradiction(dialogue, turn_index=2)

    output_file = Path("data/dialogstudio_modified/modified_sample.json")
    output_file.write_text(json.dumps(modified, indent=2))
