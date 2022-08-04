import requests
import json


def querySuggestions(query, env, authenticationURI, queryID):
    body = {"query": query, "authenticationURI": authenticationURI, "queryID": queryID}
    if env == "prod":
        url = "https://intelligence.polynomial.ai/lens_core_prod/querySuggestions"
    else:
        url = "https://intelligence.polynomial.ai/lens_core_dev/querySuggestions"
    res = requests.post(url=url, json=body)
    response = json.loads(res.text)
    if response["status"]:
        return response["response"]
    else:
        return []


if __name__ == "__main__":
    print(querySuggestions("pgs with wifi"))
