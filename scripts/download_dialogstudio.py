from datasets import load_dataset
import json
from pathlib import Path

# Config
dataset_name = "MULTIWOZ2_2"
save_dir = Path("data/dialogstudio_raw")
save_dir.mkdir(parents=True, exist_ok=True)

# Load dataset from Hugging Face
dataset = load_dataset("Salesforce/dialogstudio", dataset_name)

# Save a small sample from train split (you can also save full if preferred)
sample_data = dataset["train"].select(range(100))  # adjust range for more

# Save to local JSON
output_path = save_dir / f"{dataset_name.lower()}_sample.json"
with output_path.open("w") as f:
    json.dump(sample_data.to_list(), f, indent=2)

