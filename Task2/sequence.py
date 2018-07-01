import random
import string


random = ''.join([random.choice(string.ascii_lowercase) for i in xrange(1000000)])


print random
print ''

# for testing
x = 'j'
b = 'll'
y = 'zzz'

count1 = random.count(x)
count2 = random.count(b)
count3 = random.count(y)
print count1, count2, count3
