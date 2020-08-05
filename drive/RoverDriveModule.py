from drive import DriveModuleInterface, Speed, DriveDirection


class RoverDriveModule(DriveModuleInterface):

    def __init__(self, vehicle):
        self.__current_speed = Speed.ZERO
        self.__current_direction = DriveDirection.FORWARD
        self.__vehicle = vehicle

    async def go_forward(self, speed=Speed.FIVE):
        self.__current_direction = DriveDirection.FORWARD
        self.__current_speed = speed
        self.__vehicle.channels.overrides['4'] = 1625

    async def go_reverse(self, speed=Speed.FIVE):
        self.__current_direction = DriveDirection.REVERSE
        self.__current_speed = speed
        self.__vehicle.channels.overrides['4'] = 1390

    async def stop(self):
        self.__current_direction = DriveDirection.FORWARD
        self.__current_speed = Speed.ZERO
        self.__vehicle.channels.overrides['4'] = 1500

    @property
    def current_speed(self):
        return self.__current_speed

    @property
    def current_direction(self):
        return self.__current_direction
