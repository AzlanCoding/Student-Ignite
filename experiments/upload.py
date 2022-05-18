#upload
def upload(file=None):
    import time
    def time_convert(sec):
      mins = sec // 60
      sec = sec % 60
      hours = mins // 60
      mins = mins % 60
      print("Time Lapsed = {0}:{1}:{2}".format(int(hours),int(mins),sec))
    import time
    print("Starting...")
    start_time = time.time()
    from pydrive.auth import GoogleAuth
    from pydrive.drive import GoogleDrive
    import threading
    gauth = GoogleAuth()
    gauth.LocalWebserverAuth() # client_secrets.json need to be in the same directory as the script
    drive = GoogleDrive(gauth)
    folderName = 'DoNotDeletePhoenixStorage'
    folders = drive.ListFile({'q': "title='" + folderName + "' and mimeType='application/vnd.google-apps.folder' and trashed=false"}).GetList()
        
    for folder in folders:
        if folder['title'] == folderName:
            folderId = folder['id']

    import glob, os
    if file == None:
        from PyQt6 import QtWidgets
        from QtWidgets import QFileDialog
        #prompt
        file = QFileDialog.getOpenFileName(self, 'Open file', os.getcwd(), "video files (*.mp4 *.mov)")
    #file = "D:/Github/Student-Ignite/experiments/IMG_0792.MOV"
    with open(file,"r") as f:
        fn = os.path.basename(f.name)
        print(fn)
        file_drive = drive.CreateFile({'title':fn, 'mimetype': 'video/mp4','parents': [{'id': folderId}], 'copyRequiresWriterPermission': True, 'writersCanShare': False})
        file_drive.SetContentFile(file_loc)
        file_drive.Upload()
        file_drive.InsertPermission({
                        'type': 'anyone',
                        'value': 'anyone',
                        'role': 'reader'})
                               
    files = drive.ListFile({"q": "'" + folderId + "' in parents and trashed=false"}).GetList()
    for file in files:
        keys = file.keys()
        if file['shared'] and 'alternateLink' in keys:
            link = file['alternateLink']
        else:
            link = 'No Link Available. Check your sharing settings.'
            
        name = file['id']
        
        print('name: {}  link: {}'.format(name, link))
    end_time = time.time()
    time_lapsed = end_time - start_time
    time_convert(time_lapsed)
    return name
