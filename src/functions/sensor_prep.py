import json


def str_to_dict(str1):
    str1 = '{"' + str1\
        .replace("b", "")\
        .replace('"', '')\
        .replace("'", '')\
        .replace(",", '","')\
        .replace("=", '":"')\
        .replace("&", '","')\
        .replace("PASSKEY:", 'PASSKEY":"') + '"}'

    dict1 = json.loads(str1)

    return dict1
