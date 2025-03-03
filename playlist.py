import os
import json
import shutil
import sys

final = "Final"

def exec (cmd):
	print(f"CMD: {cmd}")
	os.system(cmd)



playlist = sys.argv[1]

def read_from (final):
	metadatas = []
	for directory in os.listdir(final):
		with open(f'{final}/{directory}/इत्तिला.json', 'rb') as info_file:
			metadata = json.load(info_file)
			metadatas.append((directory, metadata))
	return metadatas

def write_to (metadatas, final):
	for directory,metadata in metadatas:
		with open(f'{final}/{directory}/इत्तिला.json', 'w') as info_file:
			info_file.write(json.dumps(metadata, indent=4))

while True:
	metadatas = read_from(final)
	in_list = [] # (index of metadatas, score)
	out_list = []

	for i in range(len(metadatas)):
		directory, metadata = metadatas[i]

		if playlist in metadata["प्लेलिस्ट"]:
			in_list.append((i, metadata["प्लेलिस्ट"][playlist]))
		else:
			out_list.append(i)
	
	outformatted = sorted([(index, metadatas[index][0], metadatas[index][1]["क़िस्म"]) for index in out_list], key=lambda a:a[2])
	for index, name, genre in outformatted:
		print(f"{index: >3} {name : <50}{genre}")

	print("\nIn List:")
	informatted = sorted([(index, metadatas[index][0], score) for index, score in in_list], key=lambda a: a[2], reverse = True)
	for index, name, score in informatted:
		print(f"{index: >3} {name : <50}{score}")

	try:
		number = int(input("#: ").strip())
		print(f"Selected {metadatas[number][0]}")
		score = input("Score: ").strip()
	except EOFError:
		break

	if score == "": # remove
		metadatas[number][1]["प्लेलिस्ट"].pop(playlist, None)
	else:
		metadatas[number][1]["प्लेलिस्ट"][playlist] = int(score)

	write_to(metadatas, final)
