import sys

print (sys.argv)

for i in range(len(sys.argv)):
    if i == 0:
        print ("Function Name %s"% sys.argv[i])
    else:
        print ("%d argument is %s"% i, sys.argv[i])