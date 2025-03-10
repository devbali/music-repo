import sys
sys.path.append("yt-dlp")
import yt_dlp

if len(sys.argv) < 2:
    file_name_or_link = "links.txt"
    print("Links file or link not provided, using links.txt ...")
else:
    file_name_or_link = sys.argv[1]

if ".txt" not in file_name_or_link:
    yt_dlp.main(["--extract-audio", "--audio-format", "mp3", "--embed-metadata", "-o", "%(title)s.%(ext)s", file_name_or_link])
else:
    yt_dlp.main(["--extract-audio", "--audio-format", "mp3", "--embed-metadata", "-o", "%(title)s.%(ext)s", "-a", file_name_or_link])
