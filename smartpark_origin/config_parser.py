"""A class or function to parse the config file and return the values as a dictionary.

The config file itself can be any of the following formats:

- ryo: means 'roll your own' and is a simple text file with key-value pairs separated by an equals sign. For example:
```
location = "Moondalup City Square Parking"
number_of_spaces = 192
```
**you** read the file and parse it into a dictionary.
- json: a json file with key-value pairs. For example:
```json
{location: "Moondalup City Square Parking", number_of_spaces: 192}
```
json is built in to python, so you can use the json module to parse it into a dictionary.
- toml: a toml file with key-value pairs. For example:
```toml
[location]
name = "Moondalup City Square Parking"
spaces = 192
```
toml is part of the standard library in python 3.11, otherwise you need to install tomli to parse it into a dictionary.
```bash
python -m pip install tomli
```
see [realpython.com](https://realpython.com/python-toml/) for more info.

Finally, you can use `yaml` if you prefer.



"""

import json


def parse_config(config: dict) -> dict:
    """Parse the config file and return the values as a dictionary"""
    # DONE: get the configuration from a parsed file

    import json

    with open('config.json', 'r') as f:
        data = json.load(f)

    return data['CarParks'][0]
    # return {'location': data_carpark['location'], 'total_spaces': data_carpark['total-spaces'],
    #        'broker_host': data_carpark['broker'], 'broker_port': data_carpark['port']}
    # return {'location': 'TBD', 'total_spaces': 0, 'broker_host': 'TBD', 'broker_port': 0}


#c = parse_config('config.json')
#print(c)
#print("{'location': 'TBD', 'total_spaces': 0, 'broker_host': 'TBD', 'broker_port': 0}")
