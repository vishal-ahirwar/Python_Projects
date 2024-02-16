
class Mobile:
    def __init__(self) -> None:
        print("Constructor Called !")

    def __init__(self, DeviceName, RAM, ROM, BatteryPower) -> None:
        self.Name = DeviceName
        self.RAM = RAM
        self.ROM = ROM
        self.BatteryPower = BatteryPower

    def GetInfo(self):
        print(f"\nInfo About {self.Name}")
        print(
            f"Device Name : {self.Name}\nRAM : {self.RAM}GB\nROM : {self.ROM}GB\nBattery Power : {self.BatteryPower}HW")


Redmi7 = Mobile("Redmi7", 3, 8, 3500)
Vivo = Mobile("Vivo", 4, 32, 4500)

Redmi7.GetInfo()
Vivo.GetInfo()
