x = int(raw_input('Enter a number: '))

def even_odd(x):
    if x % 2 == 0:
        return 'Even'
    else:
        return 'Odd'

print even_odd(x)


'''
without function:
x = int(input("Enter a number: "))
print "Even" if x % 2 == 0 else "Odd"
'''
