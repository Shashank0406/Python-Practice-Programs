import os
import struct
import platform
import site

print(struct.calcsize("P")*8)


print(os.path.isfile("6.math.py"))


print(os.name)

print(platform.architecture())
print(platform.release())

print(site.getsitepackages())