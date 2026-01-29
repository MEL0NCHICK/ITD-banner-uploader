import requests
from config import bearer_token

url = "https://xn--d1ah4a.com/api/files/upload"
id_url = "https://xn--d1ah4a.com/api/users/me"

pic = "files/humans_boi.gif"

headers = {
        "Authorization": f"Bearer {bearer_token}",
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Mobile Safari/537.36"
    }
with open(pic, "rb") as f:
    files = {"file":(pic, f, "image/mpeg")}
    upload = requests.post(url=url, headers=headers, files=files)
    print(upload.json())
    data = {"bannerId":upload.json()['id']}

set_pic = requests.put(url=id_url, headers=headers, data=data)
print(set_pic.json())
