operation = input('Input operation "x", "+", "-" or "/"...: ')
intA = input('Input integer (A): ')
intB = input('Input integer (B): ')

print(operation + ", " + intA + ", " + intB)

if operation == 'x':
    print(int(intA) * int(intB))
elif operation == '+':
    print(int(intA) + int(intB))
elif operation == '-':
    print(int(intA) - int(intB))
elif operation == '/':
    print(int(intA)  / int(intB))
elif operation == '%':
    print(int(intA)  % int(intB))
else:
    print ('Invalid Operation Specified')