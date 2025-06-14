import azure.functions as func
import datetime
import json
import logging

app = func.FunctionApp()

<<<<<<< HEAD
@app.route(route="QueueFunction", auth_level=func.AuthLevel.ANONYMOUS)
def QueueFunction(req: func.HttpRequest) -> func.HttpResponse:
=======
@app.route(route="SqlFunction", auth_level=func.AuthLevel.ANONYMOUS)
def SqlFunction(req: func.HttpRequest) -> func.HttpResponse:
>>>>>>> 4dadf3cfa0a0f61aca9ae2ffd3fc7bb80c6b43f4
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )