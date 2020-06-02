import asyncio
from steering import SteeringModuleInterface, SteeringDirection
# from vehicle import VehicleInterface


class DummySteeringModule(SteeringModuleInterface):

    # def __init__(self, vehicle: VehicleInterface):
    def __init__(self):
        # self.vehicle = vehicle
        self.current_direction = SteeringDirection.STRAIGHT

    async def steer_straight(self, timeout_ms=0):
        self.current_direction = SteeringDirection.STRAIGHT

    async def steer_right(self, timeout_ms=0):
        self.current_direction = SteeringDirection.RIGHT
        if timeout_ms != 0:
            await asyncio.sleep(timeout_ms * 10 ** -3)
            self.current_direction = SteeringDirection.STRAIGHT

    async def steer_left(self, timeout_ms=0):
        self.current_direction = SteeringDirection.LEFT
        if timeout_ms != 0:
            await asyncio.sleep(timeout_ms * 10 ** -3)
            self.current_direction = SteeringDirection.STRAIGHT

    def get_current_direction(self):
        return self.current_direction
