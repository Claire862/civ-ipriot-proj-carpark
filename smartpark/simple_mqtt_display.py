import mqtt_device
import time
class Display(mqtt_device.MqttDevice):
    """Displays the number of cars and the temperature"""
    def __init__(self, config):
        super().__init__(config)
        self.client.on_message = self.on_message
        self.topic_qualifier = 'display'
        #subscribe to 'display'. See later how to use create topic method if there are multiple carpark
        self.client.subscribe('display')

        # list having the values for the fields = ['Available bays', 'Temperature', 'At']
        self.data2display = [0, 0, 0]
        #self.client.loop_forever()

    def display(self, *args):
        print('*' * 20)
        for val in args:
            print(val)
            time.sleep(1)

        print('*' * 20)

    def on_message(self, client, userdata, msg):
        data = msg.payload.decode()
        #self.display(*data.split(','))

        # DONE: Parse the message and extract free spaces,\
        #  temperature, time

        data_list_from_split = data.split(', ')
        data_list = []

        for item in data_list_from_split:
            key_value_list = item.split(': ')
            data_list.append(str(key_value_list[1]))

        self.data2display = data_list








if __name__ == '__main__':

    # DONE: Read config from file

    from config_parser import parse_config
    config = parse_config('config.json')

    display2 = Display(config)





