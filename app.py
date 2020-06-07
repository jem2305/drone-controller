import asyncio
from flask import Flask, redirect, jsonify
from vehicle import DummyVehicle

app = Flask(__name__,
            static_url_path='',
            static_folder='web/static',
            template_folder='web/templates')
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

loop = asyncio.get_event_loop()
vehicle = DummyVehicle()


@app.route('/')
def index():
    return redirect("/index.html", code=302)


@app.route('/forward')
def forward():
    loop.run_until_complete(vehicle.drive_module.go_forward())
    return get_vehicle_status()


@app.route('/reverse')
def backward():
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
        steeringDirection=vehicle.steering_module.current_direction.name
    )


if __name__ == '__main__':
    app.debug = True
    app.run(threaded=True)