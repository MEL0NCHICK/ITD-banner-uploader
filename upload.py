import os
import requests


url = "https://xn--d1ah4a.com/api/files/upload"
id_url = "https://xn--d1ah4a.com/api/users/me"


def upload(filename, codec, bearer_token):
    headers = {
        "Authorization": f"Bearer {bearer_token}",
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Mobile Safari/537.36"
    }
    with open(filename, "rb") as f:
        files = {
            "file":(filename, f, codec)
        }
        print("Загружаем баннер...")
        upload = requests.post(url=url, headers=headers, files=files)

        if upload.status_code == 201:
            print("Загрузили!!!")
            print(f"Статускод: {upload.status_code}")
        else:

            print(f"Ошибка сервера: ")
        print(upload.json())

        try:
            data = {"bannerId":upload.json()['id']}
        except:
            exit()


    set_pic = requests.put(url=id_url, headers=headers, data=data)
    print(set_pic.json())
    print("Загружено!!! Обнови страницу на сайте" if set_pic.status_code == 200 else f"Чет ошибка какая-то, статускод: {set_pic.status_code}")

def scandir(dir):
    files = []
    with os.scandir(dir) as fls:
        for entry in fls:
            files.append(entry)
    return files