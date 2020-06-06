import asyncio
from flask import Flask
from vehicle import DummyVehicle

app = Flask(__name__.split('.')[0])
loop = asyncio.get_event_loop()
vehicle = DummyVehicle()


@app.route('/')
def get_vehicle_status():
    status = 'Speed: {speed}\nDirection: {direction}'.format(
        speed=vehicle.drive_module.get_current_speed().name,
        direction=vehicle.steering_module.get_current_direction().name
    )
    return status

@app.route('/forward')
def forward():
    ret = loop.call_soon_threadsafe(vehicle.drive_module.go_forward(timeout_ms=5000))
    return get_vehicle_status()

@app.route('/backward')
def backward():
    ret = loop.run_until_complete(vehicle.drive_module.go_backward(timeout_ms=5000))
    return get_vehicle_status()

@app.route('/left')
def left():
    ret = loop.run_until_complete(vehicle.steering_module.steer_left(timeout_ms=5000))
    return get_vehicle_status()

@app.route('/right')
def right():
    ret = loop.run_until_complete(vehicle.steering_module.steer_right(timeout_ms=5000))
    return get_vehicle_status()

