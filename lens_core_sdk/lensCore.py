from lens_core_sdk.autoComplete import autoComplete
from lens_core_sdk.queryParser import parseQuery
from lens_core_sdk.querySuggestions import querySuggestions
from lens_core_sdk.spellCheck import spellCheck


class lensCore:
    def __init__(self):
        self.authenticationURI = None

    def setAuthenticationURI(self, uri):
        self.authenticationURI = uri
        return True

    def autoComplete(self, query):
        if not self.authenticationURI:
            return {"status": "unauthorized", "msg": "Please set authentication URI"}
        return autoComplete(query, self.authenticationURI)

    def queryParser(self, query):
        if not self.authenticationURI:
            return {"status": "unauthorized", "msg": "Please set authentication URI"}
        return parseQuery(query, self.authenticationURI)

    def querySuggestions(self, query, queryID = 1234):
        if not self.authenticationURI:
            return {"status": "unauthorized", "msg": "Please set authentication URI"}
        return querySuggestions(query, self.authenticationURI, queryID)

    def spellCheck(self, query):
        if not self.authenticationURI:
            return {"status": "unauthorized", "msg": "Please set authentication URI"}
        return spellCheck(query, self.authenticationURI)
