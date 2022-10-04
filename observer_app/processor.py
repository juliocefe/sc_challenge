import requests

def process_file_service(path):
    url = "http://127.0.0.1:8001"
    with open(path, "rb") as f:
        files = {'transactions_file': f}
        r = requests.post(url, files=files)
    print(r.text)
    return r.text