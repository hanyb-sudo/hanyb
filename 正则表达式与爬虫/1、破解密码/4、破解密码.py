import itertools
import time

passwd = ("".join(x) for x in itertools.product("0123456789", repeat=6))

while True:
    try:
        time.sleep(1)
        str = next(passwd)
        print(str)
    except StopIteration as e :
        break