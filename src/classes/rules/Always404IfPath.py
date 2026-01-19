from .Rule import Rule



class Always404IfPath(Rule):


    id = "always-404-if-path"
    description = "Always implement a response with the status code '404 Not Found' if the method contains path parameters."
    category = "standard"


    @classmethod
    def _check(cls, data):

        status_codes = data.get("status-codes", [])
        has_path_parameters = data.get("has-path-parameters", False)

        if not has_path_parameters:
            return True
        
        return "404" in status_codes