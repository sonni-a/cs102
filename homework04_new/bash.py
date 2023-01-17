input = open('input.txt', 'r')
output = open('output.txt', 'w')
n = int(input.readline()[0])
a = [int(x) for x in input.readline().split()]
for i in range(0, n):
    k = a[i]
    j = i - 1
    while j >= 0 and a[j] > k:
        a[j+1] = a[j]
        j -= 1
        a[j+1] = k
for i in a:
 output.write(str(i))
 output.write(' ')