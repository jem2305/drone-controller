from drive import DriveModuleInterface, Speed, DriveDirection


class DummyDriveModule(DriveModuleInterface):

    def __init__(self):
        self.__current_speed = Speed.ZERO
        self.__current_direction = DriveDirection.FORWARD

    async def go_forward(self, speed=Speed.FIVE):
        self.__current_direction = DriveDirection.FORWARD
        self.__current_speed = speed

    async def go_reverse(self, speed=Speed.FIVE):
        self.__current_direction = DriveDirection.REVERSE
        self.__current_speed = speed

    async def stop(self):
        self.__current_direction = DriveDirection.FORWARD
        self.__current_speed = Speed.ZERO

    @property
    def current_speed(self):
        return self.__current_speed

    @property
    def current_direction(self):
        return self.__current_direction
