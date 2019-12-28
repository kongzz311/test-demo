import math
import os
import sys

import requests

print(sys.version)
print(sys.executable)


def greet(who_to_greet):

    greeting = 'hello, {}'.format(who_to_greet)
    return greeting


print(greet('world'))
print(greet('kongzz'))

# r = requests.get('http://kongzhenzhou.com')
# print(r.status_code)

name = input("your name? ")
print("hello,", name)
