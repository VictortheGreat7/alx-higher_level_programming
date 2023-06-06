#!/usr/bin/python3

alphabet = ""
for char in range(ord('a'), ord('z') + 1):
    alphabet += chr(char)

print("{}".format(alphabet), end="")
