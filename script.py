import os
import subprocess
from ftplib import FTP

ARTIST = "Aaryan Shah"

FTP_HOST = "dl.lyricaa.ir"
FTP_USER = "musicbot"
FTP_PASS = "M@edeh1377"

DOWNLOAD_DIR = "downloads"
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

print("Downloading music...")

cmd = [
    "yt-dlp",
    "ytsearch1:" + ARTIST + " official audio",
    "-x",
    "--audio-format", "mp3",
    "-o", DOWNLOAD_DIR + "/%(title)s.%(ext)s"
]

subprocess.run(cmd)

files = os.listdir(DOWNLOAD_DIR)

if not files:
    print("No file downloaded")
    exit()

file_path = DOWNLOAD_DIR + "/" + files[0]

print("Connecting FTP...")

ftp = FTP(FTP_HOST)
ftp.login(FTP_USER, FTP_PASS)

ftp.cwd("music")

print("Uploading...")

with open(file_path, "rb") as f:
    ftp.storbinary("STOR " + files[0], f)

ftp.quit()

print("Done")
