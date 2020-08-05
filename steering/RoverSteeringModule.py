import asyncio
from steering import SteeringModuleInterface, SteeringDirection


class RoverSteeringModule(SteeringModuleInterface):

    def __init__(self, vehicle):
        self.__current_direction = SteeringDirection.STRAIGHT
        self.__vehicle = vehicle

    async def steer_straight(self, timeout_ms=0):
        self.__current_direction = SteeringDirection.STRAIGHT
        self.__vehicle.channels.overrides['1'] = 1500

    async def steer_right(self, timeout_ms=0):
        self.__current_direction = SteeringDirection.RIGHT
        self.__vehicle.channels.overrides['1'] = 1100

    async def steer_left(self, timeout_ms=0):
        self.__current_direction = SteeringDirection.LEFT
        self.__vehicle.channels.overrides['1'] = 1900

    @property
    def current_direction(self):
        return self.__current_direction