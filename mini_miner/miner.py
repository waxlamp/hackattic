import hashlib
import itertools
import json
import math
import requests


def mine(obj, diff):
    data = json.dumps(obj['data'], separators = (',', ':'))
    serial = '{"data":%s,"nonce":%%d}' % (data)

    for nonce in itertools.count(0):
        string = serial % (nonce)
        print string
        h = hashlib.sha256(string)
        digest = h.digest()

        zeros = 0
        for byte in map(ord, digest):
            if byte == 0:
                zeros += 8
            else:
                zeros += 8 - (math.floor(math.log(byte) / math.log(2)) + 1)
                break

        if zeros >= diff:
            print h.hexdigest()
            return nonce


block = requests.get('https://hackattic.com/challenges/mini_miner/problem?access_token=ae44cd88619c6ff5').json()
nonce = mine(block['block'], block['difficulty'])
r = requests.post('https://hackattic.com/challenges/mini_miner/solve?access_token=ae44cd88619c6ff5', data = json.dumps({'nonce': nonce})).json()
print r
