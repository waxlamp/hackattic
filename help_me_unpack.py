import base64
import json
import requests
import struct
import sys


def go(obj):
    string = obj['bytes']

    decode = base64.b64decode(string)

    intv = struct.unpack('<i', decode[:4])[0]
    uintv = struct.unpack('<I', decode[4:8])[0]
    shortv = struct.unpack('<hxx', decode[8:12])[0]
    floatv = struct.unpack('<f', decode[12:16])[0]
    doublev = struct.unpack('<d', decode[16:24])[0]
    big_endian_doublev = struct.unpack('>d', decode[24:32])[0]

    return {'int': intv,
            'uint': uintv,
            'short': shortv,
            'float': floatv,
            'double': doublev,
            'big_endian_double': big_endian_doublev}


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print >>sys.stderr, 'usage: help_me_unpack.py <hackattic_key>'
        sys.exit(1)

    key = sys.argv[1]

    obj = requests.get('https://hackattic.com/challenges/help_me_unpack/problem?access_token=%s' % (key)).json()
    resp = go(obj)
    print resp
    r = requests.post('https://hackattic.com/challenges/help_me_unpack/solve?access_token=%s' % (key), data = json.dumps(resp)).json()
    print r
