# Will replace every song's mp3 song with another file in the folder
# Assumes linux

import os

final = "/home/dev/Music/गीत/Final"

for directory in os.listdir(final):
	path = f'{final}/{directory}'
	num = len([f for f in os.listdir(path) 
    	if f.endswith('.mp3') and os.path.isfile(os.path.join(path, f))])
	geet = "गीत.mp3"
	if num == 2:
		os.chdir(path)
		os.system(f"rm '{geet}' && mv *.mp3 '{geet}'")
