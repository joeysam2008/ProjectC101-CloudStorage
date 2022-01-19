import os
import dropbox
from dropbox.files import WriteMode

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token
    
    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        for root, dirs, files in os.walk(file_from):

            for filename in files:
                # construct the full local path
                local_path = os.path.join(root, filename)

                # construct the full Dropbox path
                relative_path = os.path.relpath(local_path, file_from)
                dropbox_path = os.path.join(file_to, relative_path)
                    
                # upload the file
                f = open(file_from, 'rb')
                dbx.files_upload(f.read(), dropbox_path, mode=WriteMode('overwrite'))

def main():
    access_token = 'sl.BAZOugSLdbHFglBq1ziT6OnDQuC0l3Q0ABDkA_FB3xGbo8ExOLOs6xvgevIZkvkQ8Scy-DezYaWmYgyeVAATS5BkpEaiKBat1on60m1ZPogC6b98zYVoOFaJJNBiZ2uvp-z7ieSfZi1V'
    transferData = TransferData(access_token)

    file_from = input('Enter the file path to transfer: ')
    file_to = input('Enter the full path to upload to dropbox: ')
    # The full path to upload the file to, including the file name

    # API v2
    transferData.upload_file(file_from, file_to)

    print('Your file has been moved to Dropbox.')

main()