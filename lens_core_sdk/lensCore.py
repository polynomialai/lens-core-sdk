from lens_core_sdk.autoComplete import autoComplete
from lens_core_sdk.queryParser import parseQuery
from lens_core_sdk.querySuggestions import querySuggestions
from lens_core_sdk.spellCheck import spellCheck
import os
from dotenv import load_dotenv

load_dotenv(".envvar")

class lensCore:
    def __init__(self):
        self.authenticationURI = None
        self.env = os.environ["ENV"]

    def setAuthenticationURI(self, uri):
        self.authenticationURI = uri
        return True

    def autoComplete(self, query):
        if not self.authenticationURI:
            return {"status": "unauthorized", "msg": "Please set authentication URI"}
        return autoComplete(query, self.env, self.authenticationURI)

    def queryParser(self, query):
        if not self.authenticationURI:
            return {"status": "unauthorized", "msg": "Please set authentication URI"}
        return parseQuery(query, self.env, self.authenticationURI)

    def querySuggestions(self, query, queryID=1234):
        if not self.authenticationURI:
            return {"status": "unauthorized", "msg": "Please set authentication URI"}
        return querySuggestions(query, self.env, self.authenticationURI, queryID)

    def spellCheck(self, query):
        if not self.authenticationURI:
            return {"status": "unauthorized", "msg": "Please set authentication URI"}
        return spellCheck(query, self.env, self.authenticationURI)
