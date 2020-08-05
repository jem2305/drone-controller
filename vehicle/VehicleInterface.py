class VehicleInterface:

    def __init__(self):
        self.__drive_moodule = None
        self.__steering_module = None
        self.__is_connected = False

    async def connect_vehicle(self, connection_string):
        pass

    async def disconnect_vehicle(self):
        pass

    @property
    def is_connected(self):
        pass

    @property
    def drive_moodule(self):
        pass

    @property
    def steering_module(self):
        pass
