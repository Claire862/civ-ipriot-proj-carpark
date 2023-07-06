import mqtt_device
import time
class Display(mqtt_device.MqttDevice):
    """Displays the number of cars and the temperature"""
    def __init__(self, config):
        super().__init__(config)
        self.client.on_message = self.on_message
        self.topic_qualifier = 'display'
        #self.client.subscribe(self._create_topic_string())
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
        #print('this is the payload from mqtt_display')
        #print(data)
        #self.display(*data.split(','))
        # DONE: Parse the message and extract free spaces,\
        #  temperature, time

        data_list_full = data.split(', ')
        data_dict = {}
        data_list = []

        for item in data_list_full:
            key_value_list = item.split(': ')
            data_dict[key_value_list[0]] = key_value_list[1]
            data_list.append(str(key_value_list[1]))


        self.data2display = data_list
        #print(self.data2display)







if __name__ == '__main__':
    config1 = {'name': 'display',
     'location': 'L306',
     'topic-root': "lot",
     'broker': 'localhost',
     'port': 1883,
     'topic-qualifier': 'na'
     }
    # DONE: Read config from file

    from config_parser import parse_config
    config = parse_config('config.json')

    display2 = Display(config)
    display2.client.on_message = display2.on_message
    print('display init')
    display2.client.loop_forever()




