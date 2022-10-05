import requests

def process_file_service(path):
    url = "http://flask:5000"
    with open(path, "rb") as f:
        files = {'transactions_file': f}
        r = requests.post(url, files=files)
    print(r.text)
    return r.text