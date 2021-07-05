import dropbox


file_name='deploy.zip'
dropbox_path='/var/jenkins_home/workspace/pipeline@2/features/'
dbx=dropbox.Dropbox('')


with open(file_name, 'rb') as f:
    dbx.files_upload(f.read(),dropbox_path+file_name,mute=True)
