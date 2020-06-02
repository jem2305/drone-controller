import asyncio

from . import VehicleInterface
from steering import DummySteeringModule
from drive import DummyDriveModule


class DummyVehicle:

    def __init__(self):
        self.drive_module = DummyDriveModule()
        self.steering_module = DummySteeringModule()
        pass

    def do_something(self):
        asyncio.ensure_future(self.steering_module.steer_left(timeout_ms=2000))
        asyncio.ensure_future(self.drive_module.go_forward(timeout_ms=2000))
