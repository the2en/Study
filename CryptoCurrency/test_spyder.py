# Q1: Make a list of numbers from 3 to 5
list1 = list(range(3, 5 + 1))


# Q2: Use for loo``p to square and add the numbers in the list
result = 0

for i in list1:
    result += i ** 2

# Check it runs without problems
print('결과:', result)


# Q3: Define a function that does the for loop for the numbers from 1 to any number you put
def SquareAdd(x):
    output = 0
    
    for i in range(1, x + 1):
        output += i ** 2
    
    return output

# Check it runs without problems
num = int(input('Any Number: '))
answer = SquareAdd(num)

print('결과:', answer)


# Q4: Download ethereum KRW from investing.com read the file and save it as dfe
import pandas as pd

dfe = pd.read_csv('./data/ETH_KRW Bithumb Historical Data.csv')

# Check it runs without problems
print(dfe)