import asyncio
from steering import DummySteeringModule, SteeringModuleInterface
from drive import DummyDriveModule, DriveModuleInterface

steering_module = DummySteeringModule()
drive_module = DummyDriveModule()

async def do_something_with_drone():
    asyncio.ensure_future(steering_module.steer_left(timeout_ms=2000))
    asyncio.ensure_future(drive_module.go_forward(timeout_ms=2000))


def print_attributes(steering_module: SteeringModuleInterface, drive_module: DriveModuleInterface):
    print("\n\n-------------------- Drone Attributes -------------------- ")
    print("Steering Direction: " + steering_module.get_current_direction().name)
    print("Drive Speed: " + drive_module.get_current_speed().name)
    print("Drive Direction: " + drive_module.get_current_direction().name)


@asyncio.coroutine
def attribute_print_routine():
    while True:
        print_attributes(steering_module, drive_module)
        yield from asyncio.sleep(5e-1)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.create_task(attribute_print_routine())
    loop.run_until_complete(do_something_with_drone())
    loop.run_until_complete(asyncio.sleep(5))
