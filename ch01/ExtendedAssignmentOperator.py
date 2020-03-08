''' page#16 '''

orig = 5
temp = orig

'''orig = orig + 10'''

orig += 20

print (orig)
print (temp)

''' Demonstrate List'''
print ('------------------------')
orig = [1, 2, 3]
temp = orig

temp = temp + [4, 5, 6]

print (orig)
print (temp)

'''look at this : VERY IMPORTANT'''
print ('------------------------')
orig = [1, 2, 3]
temp = orig

'''
Note: += extends the original list
'''
temp += [4, 5]
'''
Note: this reassign the identified to newly constructed value
'''
temp = temp + [6, 7]

print (orig)
print (temp)