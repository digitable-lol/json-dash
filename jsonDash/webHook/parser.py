from django.forms import ValidationError
from .models import jsonNode

# TODO : refractor parser (increase speed)


def json_parser(json: dict, last_id: int):
    try:
        for i in json:
            if (type(json[i]) == dict):
                string = jsonNode(column_key=i, value='null', parent_id=last_id)
                string.save()
                json_parser(json[i], string.id)
            elif (type(json[i]) == list):
                array = jsonNode(column_key=i, value='null', parent_id=last_id)
                array.save()
                arr_id = array.id
                for j in range(0, len(json[i])):
                    if (type(json[i][j]) == dict):
                        json_parser(json[i][j], arr_id)
                    else:
                        string = jsonNode(column_key=json[i][j], value='null', parent_id=arr_id)
                        string.save()
            else:
                string = jsonNode(column_key=i, value=str(json[i]), parent_id=last_id)
                string.save()
    # TODO: incoming data validator
    except ValidationError:
        pass
