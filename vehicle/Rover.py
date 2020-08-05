from . import VehicleInterface
from steering import RoverSteeringModule, DummySteeringModule
from drive import RoverDriveModule, DummyDriveModule
from dronekit import connect


class Rover:

    def __init__(self):
        self.__vehicle = None
        self.__drive_module = DummyDriveModule()
        self.__steering_module = DummySteeringModule()
        self.__is_connected = False


    async def connect_vehicle(self, connection_string):
        self.__vehicle = connect(connection_string, wait_ready=True)
        self.__vehicle.parameters['FS_THR_ENABLE'] = 0
        self.__vehicle.parameters['FS_EKF_THRESH'] = 0
        self.__vehicle.parameters['FS_GCS_ENABLE'] = 0
        self.__vehicle.parameters['FS_CRASH_CHECK'] = 0
        self.__vehicle.parameters['RC_OPTIONS'] = 1
        self.__vehicle.parameters['RC_OVERRIDE_TIME'] = 1
        self.__vehicle.channels.overrides['1'] = 1500
        self.__vehicle.channels.overrides['4'] = 1500
        self.__vehicle.mode = VehicleMode("MANUAL")
        self.__vehicle.armed = True
        self.__is_connected = True
        self.__drive_module = RoverDriveModule(self.__vehicle)
        self.__steering_module = RoverSteeringModule(self.__vehicle)


    async def disconnect_vehicle(self):
        self.__vehicle.close()
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
