import os
import json
import shutil

from _imports import final, gen, exec, config

kisms = []
playlists = {}

def add_to_playlist(path, playlist, score):
	if playlist not in playlists:
		playlists[playlist] = [(path, score)]
	else:
		playlists[playlist].append((path, score))

def export_playlist_folder (folderpath, prefix, playlists):
	os.makedirs(f'{gen}/{folderpath}', exist_ok=True)
	for playlist in playlists:
		sortedplaylist = sorted(playlists[playlist], key = lambda a: a[1], reverse = True)
		with open(f'{gen}/{folderpath}/{playlist}.m3u','w',  encoding="utf-8") as playlistfile:
			playlistfile.write("\n".join([
				f"{prefix}{path}" for path, score in 
					sortedplaylist
				]))

try:
	shutil.rmtree(gen)
except FileNotFoundError:
	pass

for directory in os.listdir(final):
	bol = ""
 
	lyrics_filename = f'{final}/{directory}/{config["information-prompts"]["lyrics-filename"]}'
	if os.path.exists(lyrics_filename):
		with open(lyrics_filename, encoding="utf-8") as f:
			bol = f.read()

	info_filename = f'{final}/{directory}/{config["information-prompts"]["info-filename"]}'
	with open(info_filename, 'r',  encoding="utf-8") as info_file:
		print(f"Doing info file for {directory}")
		metadata = json.load(info_file)
		metadata_string = f"-metadata title=\"{directory}\" "

	kism = "Uncategorized"
	for tag in config["information-prompts"]["other-info"]:
		if tag["metadata-name"] == "genre":
			kism = metadata[tag["name"]]
		if tag["name"] in metadata and metadata[tag["name"]]:
			if tag["type"] == "str":
				metadata_string += f' -metadata {tag["metadata-name"]}="{metadata[tag["name"]]}"'
			elif tag["type"] == "list":
				metadata_string += f' -metadata {tag["metadata-name"]}="{", ".join(metadata[tag["name"]])}"'

	if bol:
		metadata_string += f" -metadata lyrics=\"{bol}\""

	if kism not in kisms: kisms.append(kism)
	dest = f"{gen}/{kism}/{directory}.mp3"
	
	song_playlists = metadata[config["information-prompts"]["playlist"]]
	for playlist in song_playlists:
		add_to_playlist(dest, playlist, song_playlists[playlist])

	os.makedirs(os.path.dirname(dest), exist_ok=True)

	exec(f"ffmpeg -i \"{final}/{directory}/{config['information-prompts']['song-filename']}\" -c copy {metadata_string} \"{dest}\"")


for playlist_path in config["playlist-exports"]:
    export_playlist_folder(playlist_path, config["playlist-exports"][playlist_path]["prefix-path"], playlists)

print(f"Made Genre folders {kisms}, and playlists {playlists.keys()}")


