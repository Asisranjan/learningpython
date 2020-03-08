import sys


for i in (sys.stdin, sys.stdout, sys.stderr):
    print (i)

print ("going via stdout")

sys.stdout.write("another way to do it")

x = input("read value via stdin")
print(x)

print ("type in value ", sys.stdin.readline()[:-2])

