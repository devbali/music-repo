# Finalize
import sys
from _imports import exec, final, config
import os
import sys
import json
try:
	import readline
except:
	pass

filename = sys.argv[1]

naam = input(f"{config['information-prompts']['name']}: ")
exec(f'mkdir "{final}/{naam}"')

suffix = input("Crop (ffmeg suffix): ")
exec(f"ffmpeg -i \"{filename}\" {suffix} \"{final}/{naam}/{config['information-prompts']['song-filename']}\"")

other_info_config = config['information-prompts']['other-info']

ittila = {
	** {
		k["name"]: input(f"{k['name']}: ") if k["type"] == "str" else input(f"{k['name']}: ").split(",")
			for k in other_info_config
	},
	config["information-prompts"]["playlist"]: {}
}

with open(f'{final}/{naam}/{config["information-prompts"]["info-filename"]}', 'w', encoding="utf-8") as convert_file:
	json.dump(ittila, convert_file,ensure_ascii=False, indent=4)
