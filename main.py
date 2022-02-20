from abc import ABC, abstractmethod


class Switchable(ABC):
    @abstractmethod
    def turn_on():
        """Method to turn on the light"""

    @abstractmethod
    def turn_off():
        """Method to turn off the light"""

class LightBulb(Switchable):
    def turn_on(self):
        print("LightBulb turned on...")

    def turn_off(self):
        print("LightBulb turned off")

class Fan(Switchable):
    def turn_on(self):
        print("Fan turned on...")

    def turn_off(self):
        print("Fan turned off")

class EletricalPowerSwitch:
    
    def __init__(self, client: Switchable) -> None:
        self.client = client
        self.on = False

    def press(self):
        if self.on:
            self.client.turn_off()
            self.on = False
        else:
            self.client.turn_on()
            self.on = True

if __name__ == "__main__":
    l = LightBulb()
    switch = EletricalPowerSwitch(l)
    switch.press()
    switch.press()

    f = Fan()
    switch = EletricalPowerSwitch(f)
    switch.press()
    switch.press()

