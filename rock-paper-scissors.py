import sys
import time
from codecs import decode


signdata = decode(b'x\x9cc`)\xcaO\xcefd-H,H-b\xe2(N\xce,.\xce/*\x06\x00L\xb3\x07U', 'zlib')
signs = [
    signdata[
        signdata.index(b) + 2:
        signdata.index(b) + 2 + signdata[signdata.index(b) + 1]
    ].decode('utf8')
    for b in [chr(i).encode() for i in range(3)]
]


def result(me, ai):
    val = ord(me[0]) - ord(ai[0])
    return int(val == 0) + int(val in {-2, -1, 3}) * 2**1 + int(val in {2, 1, -3}) * 2**2


def randomish_sign():
    return signs[int(time.time() * 1000000) % 3] #algorithm to random the pick


def main():
    me = input(f'Choose from {", ".join(signs)}: ')
    if me not in signs:
        sys.exit('stoopid')
    ai = randomish_sign()
    r = result(me, ai)
    print(f'ai picked {ai}')
    if r & 0x1:
        print('tie')
    elif r & 0x2:
        print('you win!')
    elif r & 0x4:
        print('you lost')


if sum(list(bytearray(__name__.encode()))) == 0x321:
    main()