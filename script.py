import os
import sys
from ftplib import FTP, error_perm

# ========= تنظیمات =========
artist = "Aaryan Shah"   # ← اسم خواننده
ftp_host = "dl.lyricaa.ir"
ftp_user = "musicbot"
ftp_pass = "M@edeh1377"   # ← رمز واقعی FTP
ftp_folder = "music"
# ===========================

try:
    print("🔎 Searching and downloading songs...")
    search_query = f'ytsearch5:{artist} official audio -live -remix'

    result = os.system(
        f'yt-dlp "{search_query}" '
        '-x --audio-format mp3 '
        '--audio-quality 0 '
        '-o "%(title)s.%(ext)s"'
    )

    if result != 0:
        print("❌ yt-dlp failed!")
        sys.exit(1)

    mp3_files = [f for f in os.listdir() if f.endswith(".mp3")]

    if not mp3_files:
        print("❌ No MP3 files found after download!")
        sys.exit(1)

    print(f"✅ Downloaded {len(mp3_files)} files")

    print("🌐 Connecting to FTP...")
    ftp = FTP(ftp_host)
    ftp.login(ftp_user, ftp_pass)
    print("✅ FTP login successful")

    ftp.cwd(ftp_folder)
    print(f"📂 Changed to folder: {ftp_folder}")

    for file in mp3_files:
        print(f"⬆ Uploading: {file}")
        with open(file, "rb") as f:
            ftp.storbinary(f"STOR {file}", f)

        os.remove(file)
        print(f"🗑 Removed local file: {file}")

    ftp.quit()
    print("✅✅✅ DONE SUCCESSFULLY ✅✅✅")

except error_perm as e:
    print("❌ FTP permission error:", e)
    sys.exit(1)

except Exception as e:
    print("❌ Unexpected error:", e)
    sys.exit(1)
