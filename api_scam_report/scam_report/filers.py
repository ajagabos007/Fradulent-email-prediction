import os
from datetime import datetime
def handle_uploaded_file(f):
    now = datetime.now()
    file_dir = os.path.dirname(__file__)
    path =file_dir + "/static/spam-emails/"
    uploaded_file =  now.strftime("%m_%d_%Y_%H_%M_%S")+".eml"
    uploaded_file_path = path + uploaded_file
    # return uploaded_file_path
    with open(uploaded_file_path, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    return uploaded_file_path