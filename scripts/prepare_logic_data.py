import json
from pathlib import Path

INPUT_PATH = Path("data/dialogstudio_raw/multiwoz2_2_sample.json")
OUTPUT_PATH = Path("data/dialogstudio_modified/logic_ready.json")

def format_dialogue(dialogue_obj):
    turns = []
    for turn in dialogue_obj.get("log", []):
        if "user utterance" in turn:
            turns.append({"role": "user", "utterance": turn["user utterance"]})
        if "system response" in turn:
            turns.append({"role": "system", "utterance": turn["system response"]})
    return {
        "dialogue_id": dialogue_obj.get("original dialog id", ""),
        "turns": turns
    }

def main():
    raw_data = json.load(open(INPUT_PATH))
    processed = [format_dialogue(d) for d in raw_data if "log" in d]

    with open(OUTPUT_PATH, "w") as f:
        json.dump(processed, f, indent=2)

    print(f"Saved {len(processed)} dialogues to {OUTPUT_PATH}")

if __name__ == "__main__":
    main()
