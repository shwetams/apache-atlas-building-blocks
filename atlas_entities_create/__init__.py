import logging
import algorithms.create_entity as create_entity
import json
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Creating entity.')
    swagger_link = "https://app.swaggerhub.com/apis/shwetams/apache-atlas-json-generator-entity/0.1"
    req_body = req.get_json()
    logging.info(f'Creating entity.{req}')
    print(req_body)
    entity_json = create_entity.create_entity_def(req_body)
    if entity_json is not None:
        return func.HttpResponse(json.dumps(entity_json),status_code=200,mimetype="application/json")
    else:
        return func.HttpResponse(f"Invalid Entity structure please use the structure defined in the link {swagger_link}",status_code=400)
    '''
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
    '''