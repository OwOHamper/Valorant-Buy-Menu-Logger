import os
import time

path = os.path.join(os.getenv('LOCALAPPDATA'), R'VALORANT\Saved\Logs\ShooterGame.log')

def PurchasePrint(gun, id):
    print(time.strftime("%H:%M:%S", time.localtime()) + f" | {gun.capitalize()} purchased with id: {id}")


weaponNames = {
    "Vector_C_": "stinger",
    "SubMachineGun_MP5_C_": "spectre",
    "AssaultRifle_Burst_C_": "bulldog",
    "DMR_C_": "guardian",
    "AssaultRifle_ACR_C_": "phantom",
    "AssaultRifle_AK_C_": "vandal",
    "LeverSniperRifle_C_": "marshall",
    "BoltSniper_C_": "operator",
    "LightMachineGun_C_": "ares",
    "HeavyMachineGun_C_": "odin"
}

i = 0
with open(path, "r") as file:
    file.seek(0, os.SEEK_END)
    while True:
        line = ""
        while len(line) == 0 or line[-1] != '\n':
            tail = file.readline()
            if tail == "":
                time.sleep(0.1)
                continue
            line += tail
        for weapon in weaponNames:
            if weapon in line:
                if i % 2:
                    PurchasePrint(weaponNames[weapon], line.split(weapon)[1].split()[0])
                i += 1
        if "Opening preRound7_C" in line:
            print(time.strftime("%H:%M:%S", time.localtime()) + " | Buy menu opened")
        elif "Closing preRound7_C" in line:
            print(time.strftime("%H:%M:%S", time.localtime()) + " | Buy menu closed")
        elif "Party_EnterMatchmakingQueue" in line:
            print(time.strftime("%H:%M:%S", time.localtime()) + " | Queue started")
        elif "Beginning travel to /Game/Maps/" in line:
            print(time.strftime("%H:%M:%S", time.localtime()) + " | Match found")
