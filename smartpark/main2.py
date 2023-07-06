from parking_lot import ParkingLot
from simple_mqtt_carpark import CarPark

def get_message(client, userdata, message):
    msg = message.payload.decode('UTF-8')
    print(msg)
    # if car entering
    #   process the car
    # if car exiting
    #   process the car
    # if xxx
    #   do something else

pl = CarPark()
pl.create_mqtt_client()



if __name__=='__main__':
    pl.mqtt_client.client.subscribe("lot/sensor")
    pl.mqtt_client.client.on_message = get_message
    print(pl.mqtt_client.name)
    print(pl.mqtt_client.topic)
    print(pl.location)
    print(pl.total_spaces)

    pl.mqtt_client.client.loop_forever()
