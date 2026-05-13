import os
from ftplib import FTP

# ========= تنظیمات =========
artist = "aaryan shah"   # ← اینجا اسم خواننده رو عوض کن
ftp_host = "dl.lyricaa.ir"
ftp_user = "musicbot"
ftp_pass = "M@edeh1377"   # ← رمز FTP خودتو بزار اینجا
ftp_folder = "music"
# ===========================

print("Searching and downloading songs...")

# سرچ و دانلود 5 آهنگ رسمی (حذف live/remix)
search_query = f'ytsearch5:{artist} official audio -live -remix'

os.system(
    f'yt-dlp "{search_query}" '
    '-x --audio-format mp3 '
    '--audio-quality 0 '
    '-o "%(title)s.%(ext)s"'
)

print("Connecting to FTP...")

ftp = FTP(ftp_host)
ftp.login(ftp_user, ftp_pass)
ftp.cwd(ftp_folder)

for file in os.listdir():
    if file.endswith(".mp3"):
        print("Uploading:", file)

        with open(file, "rb") as f:
            ftp.storbinary(f"STOR {file}", f)

        os.remove(file)  # پاک کردن بعد از آپلود

ftp.quit()

print("✅ Done! All files uploaded.")
