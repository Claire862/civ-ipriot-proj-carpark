import tkinter as tk
from simple_mqtt_sensor import Sensor

class CarDetector:
    """Provides a couple of simple buttons that can be used to represent a sensor detecting a car. This is a skeleton only."""

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Car Detector ULTRA")

        self.btn_incoming_car = tk.Button(
            self.root, text='🚘 Incoming Car', font=('Arial', 50), cursor='right_side', command=self.incoming_car)
        self.btn_incoming_car.pack(padx=10, pady=5)
        self.btn_outgoing_car = tk.Button(
            self.root, text='Outgoing Car 🚘',  font=('Arial', 50), cursor='bottom_left_corner', command=self.outgoing_car)
        self.btn_outgoing_car.pack(padx=10, pady=5)

        self.root.mainloop()


    def incoming_car(self):
        # DONE: implement this method to publish the detection via MQTT

        # create sensor
        detector_in = Sensor(config)
        # connect sensor
        detector_in.client.connect(detector_in.broker, detector_in.port)
        # create topic (ignored for the moment, might use it later if we need to work with multiple carpark
        topic = detector_in._create_topic_string()
        # publish message
        detector_in.client.publish('sensor', "entry " + str(detector_in.temperature))



    def outgoing_car(self):
        # DONE: implement this method to publish the detection via MQTT

        # create sensor
        detector_out = Sensor(config)
        # connect sensor
        detector_out.client.connect(detector_out.broker, detector_out.port)
        # create topic (ignored for the moment, might use it later if we need to work with multiple carpark
        topic = detector_out._create_topic_string()
        # publish message
        detector_out.client.publish('sensor', "exit " + str(detector_out.temperature))


if __name__ == '__main__':

    from config_parser import parse_config
    config = parse_config('config.json')

    CarDetector()
