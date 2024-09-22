import os

def save_image(file, upload_folder):
    """return the path of the saved file"""
    file_path = os.path.join(upload_folder, file.filename)
    file.save(file_path)
    return file_path
