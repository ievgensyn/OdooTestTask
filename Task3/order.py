vat = float(raw_input('Enter the VAT: ')) / 100
a = {397.01:1, 435.0:2, 435.0:2, 443.33:2, 443.33:2, 370.0:2, 630.0:1, 630.0:1, 630.0:2}
b = [[i, a[i]] for i in a]
print b, len(a)

v = a.keys()
print v

sum_items = [i * a[i] for i in range(len(a))]
print sum_items

def sum_total(numList):
    if len(numList) == 1:
        return numList[0]
    else:
        return numList[0] + sum_total(numList[1:])

print sum_total(sum_items) * vat
print vat

vat_sum = [i * vat for i in sum_item]
print vat_sum
