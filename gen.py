import os
import json
import shutil

final = "Final"
gen = "गीत"
def exec (cmd):
	print(f"CMD: {cmd}")
	os.system(cmd)

kisms = []
playlists = {}

def add_to_playlist(path, playlist, score):
	if playlist not in playlists:
		playlists[playlist] = [(path, score)]
	else:
		playlists[playlist].append((path, score))

try:
	shutil.rmtree(gen)
except FileNotFoundError:
	pass

for directory in os.listdir(final):
	bol = ""
	if os.path.exists(f'{final}/{directory}/बोल.txt'):
		with open(f'{final}/{directory}/बोल.txt', encoding="utf-8") as f:
			bol = f.read()

	with open(f'{final}/{directory}/इत्तिला.json', 'r',  encoding="utf-8") as info_file:
		print(f"Doing info file for {directory}")
		metadata = json.load(info_file)
		kism = metadata["क़िस्म"]
		metadata_string = f"-metadata title=\"{directory}\" -metadata genre=\"{kism}\" "

		if metadata["कलाकार"]:
			metadata_string += f' -metadata artist="{", ".join(metadata["कलाकार"])}"'
		if metadata["गीतकार"]:
			metadata_string += f' -metadata composer="{metadata["गीतकार"]}"'
		if metadata["फ़िल्म"]:
			metadata_string += f' -metadata album="{metadata["फ़िल्म"]}"'
		if "साल" in metadata and metadata["साल"]:
			metadata_string += f' -metadata year="{metadata["साल"]}"'
		if bol:
			metadata_string += f" -metadata lyrics=\"{bol}\""

		if kism not in kisms: kisms.append(kism)
		dest = f"{gen}/{kism}/{directory}.mp3"
		for playlist in metadata["प्लेलिस्ट"]:
			add_to_playlist(dest, playlist, metadata["प्लेलिस्ट"][playlist])

		os.makedirs(os.path.dirname(dest), exist_ok=True)

		exec(f"ffmpeg -i \"{final}/{directory}/गीत.mp3\" -c copy {metadata_string} \"{dest}\"")

os.makedirs(f'{gen}/प्लेलिस्ट', exist_ok=True)
os.makedirs(f'{gen}/.प्लेलिस्ट', exist_ok=True)
for playlist in playlists:
	sortedplaylist = sorted(playlists[playlist],key = lambda a: a[1],reverse = True)
	with open(f'{gen}/प्लेलिस्ट/{playlist}.m3u','w',  encoding="utf-8") as playlistfile:
		playlistfile.write("\n".join([
			f"/storage/emulated/0/Music/{path}" for path, score in 
				sortedplaylist
			]))

	with open(f'{gen}/.प्लेलिस्ट/{playlist}.m3u','w',  encoding="utf-8") as playlistfile:
		playlistfile.write("\n".join([
			f"/home/dev/Music/गीत/{path}" for path, score in 
				sortedplaylist
			]))

print(kisms)


