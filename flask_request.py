import requests

if __name__ == "__main__":
    r = requests.get("http://127.0.0.1:5000/sum/1/2")
    res = r.json()

    print(res["result"])


