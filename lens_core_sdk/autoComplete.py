import requests
import json


def autoComplete(query, authenticationURI):
    body = {"query": query, "authenticationURI": authenticationURI}
    url = "http://20.198.82.4:8084/autoComplete"
    res = requests.post(url=url, json=body)
    response = json.loads(res.text)
    if response["status"]:
        return response["response"]
    else:
        return []


if __name__ == "__main__":
    print(autoComplete("pgs with wi"))
