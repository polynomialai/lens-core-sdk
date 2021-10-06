import requests
import json


def parseQuery(query, env, authenticationURI):
    body = {"query": query, "authenticationURI": authenticationURI}
    if env == "prod":
        url = "https://lensservice.polynomial.ai/colive/queryParser"
    else:
        url = "https://lensservice.polynomial.ai/colive/dev/queryParser"
    res = requests.post(url=url, json=body)
    response = json.loads(res.text)
    if response["status"]:
        return response["response"]
    else:
        return []


if __name__ == "__main__":
    print(parseQuery("pgs with wifi"))
