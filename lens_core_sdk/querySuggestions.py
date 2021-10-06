import requests
import json


def querySuggestions(query, env, authenticationURI, queryID):
    body = {"query": query, "authenticationURI": authenticationURI, "queryID": queryID}
    if env == "prod":
        url = "https://lensservice.polynomial.ai/colive/querySuggestions"
    else:
        url = "https://lensservice.polynomial.ai/colive/dev/querySuggestions"
    res = requests.post(url=url, json=body)
    response = json.loads(res.text)
    if response["status"]:
        return response["response"]
    else:
        return []


if __name__ == "__main__":
    print(querySuggestions("pgs with wifi"))
