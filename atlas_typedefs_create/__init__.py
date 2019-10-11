import logging
import algorithms.create_entity as create_entity
import json
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    swagger_link = ""
    req_body = req.get_json()
    if req_body.get("entityDefs") is not None:
        entity_json = create_entity.create_entity_def(req_body)
        return func.HttpResponse(json.dumps(entity_json),status_code=200)
    else:
        return func.HttpResponse("Invalid Entity structure please use the structure defined in the link",status_code=400)

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Hello {name}!")
    else:
        return func.HttpResponse(
             "Please pass a name on the query string or in the request body",
             status_code=400
        )
