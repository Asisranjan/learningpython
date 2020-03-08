import sys

save_stdout = sys.stdout
fh = open("output.txt", "w")
sys.stdout = fh
while True:
    # output to stdout

    print ("yet another iteraion...")
    try:
        # reading from sys.stdin (stop with ctrl - D)
        number = input("Enter a number")
    except EOFError:
        print("\nciao")
        break
    else:
        number=int(number)
        if number == 0 :
            print("0 has no inverse", file=sys.stderr)
        else:
            print("inverse of %d is %f " % (number, 1.0 / number))

sys.stdout = save_stdout
fh.close()