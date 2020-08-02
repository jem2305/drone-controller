import asyncio
import atexit
from flask import Flask, redirect, jsonify
# from vehicle import DummyVehicle
from dronekit import connect, VehicleMode, LocationGlobalRelative

app = Flask(__name__,
            static_url_path='',
            static_folder='web/static',
            template_folder='web/templates')
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

loop = asyncio.get_event_loop()

connection_string = '192.168.1.48:14550'  # Edit to suit your needs.
vehicle = connect(connection_string, wait_ready=True)

vehicle.parameters['FS_THR_ENABLE'] = 0
vehicle.parameters['FS_EKF_THRESH'] = 0
vehicle.parameters['FS_GCS_ENABLE'] = 0
vehicle.parameters['FS_CRASH_CHECK'] = 0
vehicle.parameters['RC_OPTIONS'] = 1
vehicle.parameters['RC_OVERRIDE_TIME'] = 1

vehicle.channels.overrides['1'] = 1500
vehicle.channels.overrides['4'] = 1500

vehicle.mode = VehicleMode("MANUAL")
vehicle.armed = True


@app.route('/')
def index():
    return redirect("/index.html", code=302)


@app.route('/forward')
def forward():
    vehicle.channels.overrides['4'] = 1625
    return get_vehicle_status()


@app.route('/reverse')
def reverse():
    vehicle.channels.overrides['4'] = 1390
    return get_vehicle_status()


@app.route('/stop')
def stop():
    vehicle.channels.overrides['4'] = 1500
    return get_vehicle_status()


@app.route('/left')
def left():
    vehicle.channels.overrides['1'] = 1900
    return get_vehicle_status()


@app.route('/right')
def right():
    vehicle.channels.overrides['1'] = 1100
    return get_vehicle_status()


@app.route('/straight')
def straight():
    vehicle.channels.overrides['1'] = 1500
    return get_vehicle_status()


@app.route('/status')
def get_vehicle_status():
    return jsonify(
        speed=vehicle.drive_module.current_speed.name,
        driveDirection=vehicle.drive_module.current_direction.name,
        steeringDirection=vehicle.steering_module.current_direction.name
    )


def vehicle_close_handler():
    vehicle.close()


atexit.register(vehicle_close_handler)


if __name__ == '__main__':
    app.debug = True
    app.run(threaded=True)
