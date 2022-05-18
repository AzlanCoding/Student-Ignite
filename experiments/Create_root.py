def makeRoot():
    from pydrive.auth import GoogleAuth
    from pydrive.drive import GoogleDrive

    gauth = GoogleAuth()
    gauth.LocalWebserverAuth() # client_secrets.json need to be in the same directory as the script
    drive = GoogleDrive(gauth)

    #file_metadata = {'name': "DoNotDeleteIgniteStorage",'mimeType': 'application/vnd.google-apps.folder'}

    folder = drive.CreateFile({'name': "DoNotDeleteIgniteStorage",'mimeType': 'application/vnd.google-apps.folder'})
    folder.Upload()

    folder = drive.CreateFile({'name': "DoNotDeletePhoenixStorage",'mimeType': 'application/vnd.google-apps.folder'})
    folder.Upload()
makeRoot()
