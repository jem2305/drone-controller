import asyncio
import atexit
from flask import Flask, redirect, jsonify
from vehicle import Rover, DummyVehicle

app = Flask(__name__,
            static_url_path='',
            static_folder='web/static',
            template_folder='web/templates')
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

loop = asyncio.get_event_loop()

connection_string = '192.168.1.48:14550'  # Edit to suit your needs.

vehicle = Rover()


@app.route('/')
def index():
    return redirect("/index.html", code=302)


@app.route('/connect')
def connect():
    loop.run_until_complete(vehicle.connect_vehicle(connection_string))
    return get_vehicle_status()


@app.route('/disconnect')
def disconnect():
    loop.run_until_complete(vehicle.disconnect_vehicle())
    return get_vehicle_status()


@app.route('/forward')
def forward():
    loop.run_until_complete(vehicle.drive_module.go_forward())
    return get_vehicle_status()


@app.route('/reverse')
def reverse():
    loop.run_until_complete(vehicle.drive_module.go_reverse())
    return get_vehicle_status()


@app.route('/stop')
def stop():
    loop.run_until_complete(vehicle.drive_module.stop())
    return get_vehicle_status()


@app.route('/left')
def left():
    loop.run_until_complete(vehicle.steering_module.steer_left())
    return get_vehicle_status()


@app.route('/right')
def right():
    loop.run_until_complete(vehicle.steering_module.steer_right())
    return get_vehicle_status()


@app.route('/straight')
def straight():
    loop.run_until_complete(vehicle.steering_module.steer_straight())
    return get_vehicle_status()


@app.route('/status')
def get_vehicle_status():
    return jsonify(
        speed=vehicle.drive_module.current_speed.name,
        driveDirection=vehicle.drive_module.current_direction.name,
        steeringDirection=vehicle.steering_module.current_direction.name,
        isConnected=vehicle.is_connected
    )


atexit.register(disconnect)


if __name__ == '__main__':
    app.debug = True
    app.run(threaded=True)
