'''import upload
import Create_root
Create_root.makeRoot()
upload.upload()'''
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
gauth.LocalWebserverAuth() 
drive = GoogleDrive(gauth)
folder_id = '1vgHEYBppI77rNRElkojaf1h4pJCSfELz'

file_metadata = {
  'name': 'test_folder',
  'parents': [folder_id],
  'mimeType': 'application/vnd.google-apps.folder'
}

folder = drive.CreateFile(file_metadata)
folder.Upload()
