import random

start = input('Please input the start value: ')
end = input('Please input the end value: ')
start = int(start)
end = int(end)

r = random.randint(start, end)
count = 0

while True:
    count += 1 # count = count + 1! 
    num = input('Guess the number: ')
    num = int(num)
    if num == r:
        print('Your Right')
        print ('This is your', count, 'times')
        break
    elif num > r:
        print('Small than your input')
    else:
        print('Bigger than your input')
    print ('This is your', count, 'times')
