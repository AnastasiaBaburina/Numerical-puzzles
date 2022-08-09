from math import log2

num_letter = {
    0:'a', 1:'b', 2:'c', 3:'d', 4:'e', 5:'f', 6:'g', 7:'h', 8:'i',
    9:'j', 10:'k', 11:'l', 12:'m', 13:'n', 14:'o', 15:'p', 16:'q', 
    17:'r', 18:'s', 19:'t', 20:'u', 21:'v', 22:'w', 23:'x', 24:'y', 25:'z', 26:' ',
}

f1 = open("input.txt", "r")
f1.seek(0)
a = f1.readline()
b  =f1.readline()
n = int(a)
W = [int(x) for x in b.split()]

result = []
result.append(num_letter[int(log2(W[0]))])
t = 0
for i in range(1,n):
    z = abs(W[i]-W[t])
    result.append(num_letter[int(log2(z))])
    t += 1

res=''
for i in range(0,n):
    res+=result[i]

print(res)
f1.close()