from gpiozero import DigitalOutputDevice
import constants


def washer():
    try:
        relayWasher = DigitalOutputDevice(constants.WASHER)
        relayWasher.blink(constants.CLOSE_TIME, constants.OPEN_TIME, 1, False)
        relayWasher.close()
    except GPIOZeroError:
        return 1
    return 0


def dryer():
    try:
        relayDryer = DigitalOutputDevice(constants.DRYER)
        relayDryer.blink(constants.CLOSE_TIME, constants.OPEN_TIME, 1, False)
        relayWasher.close()
    except GPIOZeroError:
        return 1
    return 0
