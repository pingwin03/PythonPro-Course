wzrost = int(input("Podaj wazrost w cm:"))
opiekun = input("czy jest opiekun? (tak/nie):")

Wchodzimy = (wzrost >= 120 and opiekun == "tak") or (wzrost >= 160)
print(Wchodzimy)