vat = int(raw_input('Enter the VAT: ')) / 100
a = {397.01:1, 435.0:2, 435.0:2, 443.33:2, 443.33:2, 370.0:2, 630.0:1, 630.0:1, 630.0:2}
b = [[i, a[i]] for i in a]

sum_item = [i * a[i] for i in a]
print sum_item

def sum_total(numList):
    if len(numList) == 1:
        return numList[0]
    else:
        return numList[0] + sum_item_total(numList[1:])

print sum_total(sum_item)
