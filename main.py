import rook
import random

def kaki():
    x = random.randint(0,10)
    x += 1
    return x

if __name__ == '__main__':
    rook.start(token='f7660f39b7396690e332d9cc4ba1f3e3b5c605dc550fbe1e54ad02d2202c0ef3', labels={"env":"dev"})
    x = 0
    while True:
        x = kaki()
        print(f"x {x}")
    print(f"number {x}")