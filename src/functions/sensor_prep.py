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


def str_map_emb(input_str, timestr):

    convertedDict = str_to_dict(input_str)

    sensorDict = {
        'soilmoisture1': float(convertedDict['soilmoisture1']),
        'soilatt1': float(convertedDict['soilatt1']),
        'soilmoisture2': float(convertedDict['soilmoisture2']),
        'soilatt2': float(convertedDict['soilatt2']),
        'soilmoisture3': float(convertedDict['soilmoisture3']),
        'soilatt3': float(convertedDict['soilatt3'])
    }

    outputDict = {
        'stationtype': str(convertedDict['stationtype']),
        'eventtime': str(convertedDict['dateutc']),
        'processingtime': timestr,
        'tempinf': float(convertedDict['tempinf']),
        'humidityin': float(convertedDict['humidityin']),
        'aromrelin': float(convertedDict['aromrelin']),
        'aromasin': float(convertedDict['aromasin']),
        'freq': str(convertedDict['freq']),
        'model': str(convertedDict['model']),
        'soilsensors': sensorDict,
        'id': timestr + 'station' + '0'
    }

    return outputDict
