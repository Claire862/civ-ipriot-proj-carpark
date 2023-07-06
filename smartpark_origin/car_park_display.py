import random
import threading
import time
from windowed_display import WindowedDisplay
import paho.mqtt.client as paho
from simple_mqtt_sub import on_message_received, on_connection
from mqtt_device import MqttDevice


class CarParkDisplay:
    """Provides a simple display of the car park status. This is a skeleton only. The class is designed to be customizable without requiring and understanding of tkinter or threading."""
    # determines what fields appear in the UI
    fields = ['Available bays', 'Temperature', 'At']

    def __init__(self):
        self.window = WindowedDisplay(
            'Moondalup', CarParkDisplay.fields)
        updater = threading.Thread(target=self.check_updates)
        updater.daemon = True
        updater.start()
        self.window.show()

    def check_updates(self):

        # TODO: This is where you should manage the MQTT subscription

        #car_park_display = MqttDevice(config)
        #car_park_display.client.connect(car_park_display.broker, car_park_display.port)
        #topic = car_park_display._create_topic_string()
        #print(topic)

        #BROKER, PORT = "127.0.0.1", 1883

        #car_park_display.client.on_message = on_message_received
        #car_park_display.client.on_connect = on_connection
        #car_park_display.client.connect(BROKER, PORT)
        #car_park_display.client.subscribe(car_park_display._create_topic_string())
        #client.loop_forever()

        #print(on_message_received)
        #print(on_connection)





        while True:
            # NOTE: Dictionary keys *must* be the same as the class fields
            field_values = dict(zip(CarParkDisplay.fields, [
                f'{random.randint(0, 150):03d}',
                f'{random.randint(0, 45):02d}℃',
                time.strftime("%H:%M:%S")]))
            # Pretending to wait on updates from MQTT
            time.sleep(random.randint(1, 10))




            # When you get an update, refresh the display.
            self.window.update(field_values)


if __name__ == '__main__':
    from config_parser import parse_config
    config = parse_config('config.json')


    CarParkDisplay()
