import requests
import sys
import os

url = 'http://localhost:8888/'


def upload_file(filepath: str):
    if os.path.exists(filepath):
        files = {'file': open(filepath, 'rb')}
        r = requests.post(url, files=files)
        if r.status_code == 200:
            print("Successfully uploaded")
        else:
            print("Incorrect filepath")
    else:
        print("Incorrect filepath")


def list_files():
    r = requests.get(f"{url}/files")
    if r.status_code == 200:
        files = r.json()
        for file in files:
            print(file)


if __name__ == '__main__':
    if len(sys.argv) == 3 and sys.argv[1] == 'upload':
        upload_file(sys.argv[2])
    elif len(sys.argv) == 2 and sys.argv[1] == 'list':
        list_files()


# python3 screwdriver.py upload data/audio_1.wav
# python3 screwdriver.py upload data/audio_2.mp3
# python3 screwdriver.py upload data/audio_3.mp3
# python3 screwdriver.py upload data/image.jpg
