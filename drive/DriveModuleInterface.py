from drive.Speed import Speed


class DriveModuleInterface:

    def __init__(self):
        self.__current_speed = None
        self.__current_direction = None
        pass

    async def go_forward(self, speed: Speed):
        pass

    async def go_reverse(self, speed: Speed):
        pass

    async def stop(self, speed: Speed):
        pass

    @property
    def current_speed(self) -> Speed:
        pass

    @property
    def current_direction(self):
        pass

