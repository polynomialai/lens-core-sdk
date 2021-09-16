import requests
import json


def querySuggestions(query, authenticationURI, queryID):
    body = {"query": query, "authenticationURI": authenticationURI, "queryID":queryID}
    url = "http://20.198.82.4:8084/querySuggestions"
    res = requests.post(url=url, json=body)
    response = json.loads(res.text)
    if response["status"]:
        return response["response"]
    else:
        return []


if __name__ == "__main__":
    print(querySuggestions("pgs with wifi"))
