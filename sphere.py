# inspiration code for Python Unit Testing Project

import math

def surfaceArea(radius):
    # return 4 * math.pi * radius ** 2
    pass

def volume(radius):
    volume=(4/3) * math.pi * radius ** 3
    return volume

def prompt():
    print()
    print("------------------------------------------------------------")
    print("PYTHON PROGRAM TO FIND THE VOLUME OF A SPHERE")
    print("------------------------------------------------------------")
    radius = int(input("Please Enter the radius :"))
    
    print("\nThe Volume of a Sphere = ", volume(radius))

if __name__ == '__main__':
    prompt()