#Try to download and play a video from google drive at same time
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import threading
gauth = GoogleAuth()
gauth.LocalWebserverAuth() # client_secrets.json need to be in the same directory as the script
drive = GoogleDrive(gauth)
def time_convert(sec):
  mins = sec // 60
  sec = sec % 60
  hours = mins // 60
  mins = mins % 60
  print("Time Lapsed = {0}:{1}:{2}".format(int(hours),int(mins),sec))
import time
input("Press Enter to start")
start_time = time.time()
file6 = drive.CreateFile({'id': "1fxitus41l9ET2YeMYn25vJAfMG6ZWvWH"})
file6.GetContentFile('IMG_0792.MOV')
end_time = time.time()
time_lapsed = end_time - start_time
time_convert(time_lapsed)
