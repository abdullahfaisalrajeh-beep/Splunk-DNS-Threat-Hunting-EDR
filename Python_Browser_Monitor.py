import pygetwindow as gw
import psutil
import time

# قائمة الكلمات المحظورة (تطوير لما في الصورة 1)
BANNED = ["facebook", "fb.com", "instagram", "twitter"]
BROWSERS = ["chrome.exe", "msedge.exe", "firefox.exe"]

def start_guard():
    while True:
        try:
            titles = gw.getAllTitles()
            for title in titles:
                # إذا ظهرت الكلمة في عنوان النافذة
                if any(word in title.lower() for word in BANNED):
                    for proc in psutil.process_iter(['name']):
                        if proc.info['name'].lower() in BROWSERS:
                            proc.terminate()
        except:
            pass
        time.sleep(0.5)

if __name__ == "__main__":
    start_guard()