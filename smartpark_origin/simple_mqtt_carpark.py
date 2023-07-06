from datetime import datetime

import mqtt_device
import paho.mqtt.client as paho
from paho.mqtt.client import MQTTMessage


class CarPark(mqtt_device.MqttDevice):
    """Creates a carpark object to store the state of cars in the lot"""

    def __init__(self, config):
        super().__init__(config)
        self.total_spaces = config['total-spaces']
        self.total_cars = config['total-cars']
        self._temperature = None
        self.client.on_message = self.on_message
        self.client.subscribe('sensor')
        #self.client.subscribe(self.topic)
        print(self.topic)

        self.client.loop_forever()




    @property
    def available_spaces(self):
        available = self.total_spaces - self.total_cars
        return max(available, 0)

    @property
    def temperature(self):
        return self._temperature


    
    @temperature.setter
    def temperature(self, value):
        self._temperature = value
        
    def _publish_event(self):
        readable_time = datetime.now().strftime('%H:%M')
        print(
            (
                f"TIME: {readable_time}, "
                + f"SPACES: {self.available_spaces}, "
                + f"TEMPC: {self._temperature} "
            )
        )
        message = (
            f"TIME: {readable_time}, "
            + f"SPACES: {self.available_spaces}, "
            + f"TEMPC: {self._temperature}"
        )
        self.client.publish('display', message)
        print('This is message from carpark')
        print(message)

    def on_car_entry(self):
        self.total_cars += 1
        self._publish_event()



    def on_car_exit(self):
        self.total_cars -= 1
        self._publish_event()

    def on_message(self, client, userdata, msg: MQTTMessage):
        payload = msg.payload.decode()
        print(payload)

        # DONE : Extract temperature from payload
        payload_list = payload.split()
        self._temperature = payload_list[1]

        if 'exit' in payload:
            self.on_car_exit()
        else:
            self.on_car_entry()

if __name__ == '__main__':

    config1 = {'name': "raf-park",
              'total-spaces': 130,
              'total-cars': 0,
              'location': 'L306',
              'topic-root': "lot",
              'broker': 'localhost',
              'port': 1883,
              'topic-qualifier': 'entry',
              'is_stuff': False
              }

    # DONE: Read config from file
    from config_parser import parse_config
    config = parse_config('config.json')






    car_park = CarPark(config)
    print("Carpark initialized")


