def squareInteger(incomingInteger):
    incomingInteger = incomingInteger ** 2
    return incomingInteger

incomingInteger = 5             #This variable's name has changed!
#squareInteger(incomingInteger)
b = 5
print(hex(id(incomingInteger)),hex(id(b)))
