import os
import json

with open("config.json", "r") as f:
    config = json.load(f)

final = config.get("intermediate-dir", "Final")
gen = config.get("output-dir", "गीत")

def exec (cmd):
	print(f"CMD: {cmd}")
	os.system(cmd)

os.makedirs(final, exist_ok=True)
os.makedirs(gen, exist_ok=True)
