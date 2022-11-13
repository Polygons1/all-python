import time

y = time.localtime()[0]
m = time.localtime()[1]
d = time.localtime()[2]
hr = time.localtime()[3]
mi = time.localtime()[4]
sec = time.localtime()[5]

print(hr, ':', mi, ':', sec)
print(d, '/', m, '/', y)