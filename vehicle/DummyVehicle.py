import asyncio

from . import VehicleInterface
from steering import DummySteeringModule
from drive import DummyDriveModule


class DummyVehicle:

    def __init__(self):
        self.__vehicle = None
        self.__drive_module = DummyDriveModule()
        self.__steering_module = DummySteeringModule()
        self.__is_connected = False
        pass


    async def connect_vehicle(self, connection_string):
        self.__is_connected = True


    async def disconnect_vehicle(self):
        self.__is_connected = False


    @property
    def is_connected(self):
        return self.__is_connected


    @property
    def drive_module(self):
        return self.__drive_module


    @property
    def steering_module(self):
        return self.__steering_module
