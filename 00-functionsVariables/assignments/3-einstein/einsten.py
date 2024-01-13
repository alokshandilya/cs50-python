def calculateE(m, c):
    e = m * (c**2)
    return e


def main():
    mass = int(input("m : "))
    speed_of_light = 300000000

    energy = calculateE(mass, speed_of_light)
    print(energy)


main()
