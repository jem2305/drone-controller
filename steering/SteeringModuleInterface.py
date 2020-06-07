from steering import SteeringDirection


class SteeringModuleInterface:

    def __init__(self):
        self.__current_direction = None
        pass

    async def steer_straight(self, timeout_ms: int):
        pass

    async def steer_right(self, timeout_ms: int):
        pass

    async def steer_left(self, timeout_ms: int):
        pass

    @property
    def current_direction(self) -> SteeringDirection:
        pass
