from dotenv import load_dotenv
from pathlib import Path
import os
import csv
import json

load_dotenv()
print(f"API_KEY password : {os.getenv('API_KEY')}")

data_directory = Path("data")
input_file = data_directory / "logs_bruts.json"
print(f"I'm reading {input_file}")

try:
    with open(input_file, "r", encoding="utf-8") as f:
        data = json.load(f)
        print(f"There are {len(data)} raw lines.")
except FileNotFoundError:
    print(f"File not found : {input_file}")
    data = []

errors = [line for line in data if line["status"] == "ERROR"]
print(f'There are {len(errors)} "ERROR" lines')

output_directory = Path("output")
output_directory.mkdir(exist_ok=True)
output_file = output_directory / "logs_cleared.csv"

with open(output_file, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["id", "message", "status"])
    writer.writeheader()
    writer.writerows(errors)

print(f"Result in {output_file}")