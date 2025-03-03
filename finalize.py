# Finalize
import os
import sys
import json
try:
	import readline
except:
	pass

final = "Final"

def exec (cmd):
	print(f"CMD: {cmd}")
	os.system(cmd)

filename = sys.argv[1]

naam = input("नाम: ")
exec(f'mkdir "{final}/{naam}"')

suffix = input("Crop (ffmeg suffix): ")
exec(f"ffmpeg -i \"{filename}\" {suffix} \"{final}/{naam}/गीत.mp3\"")

ittila = {
	"कलाकार": input("कलाकार: ").split(","),
	"गीतकार": input("गीतकार: "),
	"बोल": input("बोल: "),
	"फ़िल्म": input("फ़िल्म: "),
	"क़िस्म": input("क़िस्म: "),
	"साल": input("साल: "),
	"प्लेलिस्ट": {}
}

with open(f'{final}/{naam}/इत्तिला.json', 'w', encoding="utf-8") as convert_file:
     json.dump(ittila, convert_file,ensure_ascii=False, indent=4)
