from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive


def Gdrive():
    def f():
        gauth = GoogleAuth()
        gauth.LocalWebserverAuth() # client_secrets.json need to be in the same directory as the script
        drive = GoogleDrive(gauth)
        #return self
    #def test(self):
        file1 = drive.CreateFile({'title': 'AuthTest.txt'})  # Create GoogleDriveFile instance with title 'Hello.txt'.
        file1.SetContentString('File used for testing') # Set content of the file from given string.
        file1.Upload()
        file1.Trash()
    #def tried():
        file_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
        for file1 in file_list:
          print('title: %s, id: %s' % (file1['title'], file1['id']))
    f()
Gdrive()
#d.test()
#d.tried()
