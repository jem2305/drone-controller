import asyncio
from flask import Flask
from vehicle import DummyVehicle

app = Flask(__name__.split('.')[0])
loop = asyncio.get_event_loop()
vehicle = DummyVehicle()


@app.route('/')
def index():
    return vehicle.drive_module.get_current_speed().name


@app.route('/doSomething')
def do_something():
    ret = loop.run_until_complete(vehicle.drive_module.go_forward(timeout_ms=10000))
    return ret.name
