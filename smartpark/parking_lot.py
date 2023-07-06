from config_parser import parse_config, get_config
from mqtt_device import MqttDevice



class ParkingLot:

    def __init__(self):
        self.location = None  #: str
        self.total_spaces = None  #: int
        self.available_spaces = None  #: int
        self.mqtt_client = None  #: MQTTClient


    def create_mqtt_client(self):
        filename = "config.toml"
        # read config file
        config = parse_config(get_config(filename), 'broker')
        # instantiate an mqtt device
        mqtt_device = MqttDevice(config)
        # assign device to th mqtt client instance variable
        self.mqtt_client = mqtt_device
        # get the location details
        location = config['location']
        location_config = parse_config(get_config(filename), location)
        self.location = location_config['name']
        self.total_spaces = location_config['total-spaces']

    def enter(self):  # -> None
        self.available_spaces = max(self.available_spaces - 1, 0)

    def exit(self):  # -> None
        self.available_spaces = self.available_spaces + 1

    def publish_update(self):  # -> None
        pass



