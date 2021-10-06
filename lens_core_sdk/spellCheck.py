import requests
import json


def spellCheck(query, env, authenticationURI):
    body = {"query": query, "authenticationURI": authenticationURI}
    if env == "prod":
        url = "https://lensservice.polynomial.ai/colive/spellCheck"
    else:
        url = "https://lensservice.polynomial.ai/colive/dev/spellCheck"
    res = requests.post(url=url, json=body)
    response = json.loads(res.text)
    if response["status"]:
        return response["response"]
    else:
        return []


if __name__ == "__main__":
    print(spellCheck("pgs with wfi"))
