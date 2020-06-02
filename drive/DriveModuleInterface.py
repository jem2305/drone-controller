from drive.Speed import Speed


class DriveModuleInterface:

    # def __init__(self, vehicle):
    def __init__(self):
        pass

    async def go_forward(self, speed: Speed, timeout_ms: int):
        pass

    async def go_backward(self, speed: Speed, timeout_ms: int):
        pass

    async def stop(self, speed: Speed, timeout_ms: int):
        pass

    def get_current_speed(self):
        pass

    def get_current_direction(self):
        pass

