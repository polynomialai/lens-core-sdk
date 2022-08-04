import requests
import json


def autoComplete(query, env, authenticationURI):
    body = {"query": query, "authenticationURI": authenticationURI}
    if env == "prod":
        url = "https://intelligence.polynomial.ai/lens_core_prod/autoComplete"
    else:
        url = "https://intelligence.polynomial.ai/lens_core_dev/autoComplete"
    res = requests.post(url=url, json=body)
    response = json.loads(res.text)
    if response["status"]:
        return response["response"]
    else:
        return []


if __name__ == "__main__":
    print(autoComplete("pgs with wi"))
