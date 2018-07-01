import random
import string


random = ''.join([random.choice(string.ascii_lowercase) for i in xrange(1000000)])


count = random.count(raw_input())
print count
