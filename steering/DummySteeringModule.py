import asyncio
from steering import SteeringModuleInterface, SteeringDirection


class DummySteeringModule(SteeringModuleInterface):

    def __init__(self):
        self.__current_direction = SteeringDirection.STRAIGHT

    async def steer_straight(self, timeout_ms=0):
        self.__current_direction = SteeringDirection.STRAIGHT

    async def steer_right(self, timeout_ms=0):
        self.__current_direction = SteeringDirection.RIGHT
        if timeout_ms != 0:
            await asyncio.sleep(timeout_ms * 10 ** -3)
            self.__current_direction = SteeringDirection.STRAIGHT

    async def steer_left(self, timeout_ms=0):
        self.__current_direction = SteeringDirection.LEFT
        if timeout_ms != 0:
            await asyncio.sleep(timeout_ms * 10 ** -3)
            self.__current_direction = SteeringDirection.STRAIGHT

    @property
    def current_direction(self):
        return self.__current_direction
