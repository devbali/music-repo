# Will replace every song's mp3 song with another file in the folder
# Assumes linux

import os
from _imports import final, config

for directory in os.listdir(final):
	path = os.path.join(final, directory)
	num = len([f for f in os.listdir(path) 
		if os.path.isfile(os.path.join(path, f)) and f.endswith('.mp3')])

	geet = config["information-prompts"]["song-filename"]
	if num == 2:
		os.chdir(path)
		os.system(f"rm '{geet}' && mv *.mp3 '{geet}'")
		print(f"Replaced in {directory}")
