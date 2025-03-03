import subprocess
import os

final = "/home/dev/Music/गीत/Final"

for directory in os.listdir(final):
	path = f'{final}/{directory}'
	geet = "गीत.mp3"
	subprocess.run(['python', '/home/dev/Music/prayog-e qawaal/fft_film.py', 
    	os.path.join(path, geet), os.path.join(path, "चलचित्र")])
