import requests
import json


def spellCheck(query, authenticationURI):
    body = {"query": query, "authenticationURI": authenticationURI}
    url = "http://20.198.82.4:8084/spellCheck"
    res = requests.post(url=url, json=body)
    response = json.loads(res.text)
    if response["status"]:
        return response["response"]
    else:
        return []


if __name__ == "__main__":
    print(spellCheck("pgs with wfi"))
