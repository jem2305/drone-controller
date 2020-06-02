import asyncio

from drive import DriveModuleInterface, Speed, DriveDirection
# from vehicle import VehicleInterface


class DummyDriveModule(DriveModuleInterface):

    # def __init__(self, vehicle: VehicleInterface):
    def __init__(self):
        # self.vehicle = vehicle
        self.current_speed = Speed.ZERO
        self.current_direction = DriveDirection.FORWARD

    async def go_forward(self, timeout_ms=0, speed=Speed.FIVE):
        self.current_direction = DriveDirection.FORWARD
        self.current_speed = speed

        if timeout_ms != 0:
            await asyncio.sleep(timeout_ms * 10 ** -3)
            self.current_speed = Speed.ZERO

    async def go_backward(self, timeout_ms=0, speed=Speed.FIVE):
        self.current_direction = DriveDirection.BACKWARD
        self.current_speed = speed

        if timeout_ms != 0:
            await asyncio.sleep(timeout_ms * 10 ** -3)
            self.current_speed = Speed.ZERO

    async def stop(self):
        self.current_speed = Speed.ZERO

    def get_current_speed(self):
        return self.current_speed

    def get_current_direction(self):
        return self.current_direction
