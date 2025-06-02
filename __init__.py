import logging
import azure.functions as func

def main(req: func.HttpRequest) -> dict:
    name = req.params.get('name')
    email = req.params.get('email')

    return {
        "name": name,
        "email": email
    }
