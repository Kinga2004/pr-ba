import main as w

v1 = w.Vector()
v1.create()
print (v1)

v2 = w.Vector()
v2.read_values([1,2,3])
print (v2)

print (v1+v2)
print (v1-v2)
print (v2*2)

print (v2.length())
print (v2.sum())
print (v2.multi(v1))

print (1 in v2)
print (v1[1])
