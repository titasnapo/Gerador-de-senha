import random
import string

import time
tamanho = 16

chars = string.ascii_letters + string.digits + '.,@#$%&*()-+=ç?/<>[]'

rnd = random.SystemRandom()

print(''.join(rnd.choice(chars) for i in range(tamanho)))

time.sleep(40)