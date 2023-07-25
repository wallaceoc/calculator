def perform_calc(operation, intA, intB):    
    if operation == 'x':
        return int(intA) * int(intB)
    elif operation == '+':
        return int(intA) + int(intB)
    elif operation == '-':
        return int(intA) - int(intB)
    elif operation == '/':
        return int(intA) / int(intB)
    else:
        return ('Invalid Operation Specified: ' + operation)

def read_file():
    with open ("step_2.txt", 'r') as f:
        lines = f.read().splitlines()

    return lines

def step2():
    lines = read_file()

    result = 0
    for line in lines:
        tuple = line.split()
        result += perform_calc(tuple[1], tuple[2], tuple[3])

    print(result) 

def step3():
    file = read_file()

    lines = set()
    line_count = 0    
    for line in file:
        line_count+=1
        tuple = line.split()
        if(str(tuple) in lines):
            print("Duplicate line at: " + str(line_count))
            break
       
        lines.add(str(tuple))
        if len(tuple) > 2:
            next_line = perform_calc(tuple[2], tuple[3], tuple[4])
        else:
            next_line = tuple[1]

# run step 2
print("Step2 starting")
#step2()
print("Step2 completed")

# run step 3
print("Step3 starting")
step3()
print("Step3 completed")