def ksa(key):
    state = [i for i in range(256)]
    j = 0

    for i in range(256):
        j = (j + state[i] + key[i % len(key)]) % 256
        state[i], state[j] = state[j], state[i]

    return state

def prga(state):
    i = 0
    j = 0

    while True:
        i = (i + 1) % 256
        j = (j + state[i]) % 256
        state[i], state[j] = state[j], state[i]
        out = state[(state[i] + state[j]) % 256]
        yield out

def get_keystream(key):
    state = ksa(key)
    return prga(state)

def encrypt(plaintext):
    key = [c for c in range(16)]
    keystream = get_keystream(key)

    result = ''
    for c in plaintext:
        if type(c) is int:
            result += ("%02X" % (c ^ next(keystream)))
        else:
            result += ("%02X" % (ord(c) ^ next(keystream)))

    return result