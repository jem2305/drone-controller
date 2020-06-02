from steering import SteeringDirection
# from vehicle import VehicleInterface


class SteeringModuleInterface:

    # def __init__(self, vehicle: VehicleInterface):
    def __init__(self):
        pass

    async def steer_straight(self, timeout_ms: int):
        pass

    async def steer_right(self, timeout_ms: int):
        pass

    async def steer_left(self, timeout_ms: int):
        pass

    def get_current_direction(self) -> SteeringDirection:
        pass
