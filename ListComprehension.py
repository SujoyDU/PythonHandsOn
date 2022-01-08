#create a grid of 2*3

grid=[[0,0,0],
      [0,0,0]]

n_rows=2
n_columns=3

gridLoop=[]
for _ in range(n_rows):
    curr_row = []
    for _ in range(n_columns):
        curr_row.append(0)
    gridLoop.append(curr_row)

print(gridLoop)

print([[0 for _ in range(n_columns)] for _ in range(n_rows)])

## find the odd numbers in a list
lst = [1,-5,3,2,4]
print([num for num in lst if (num % 2 == 1)])
print([(num % 2 == 1) for num in lst])

##find if there is an odd number in the list
print(any([(lambda x: x%2 == 1)(num) for num in lst]))
print(any([(num % 2 == 1) for num in lst]))

#find if all numbers are odd
print(all([(lambda x: x%2 ==1) (num) for num in lst]))

#find the maximum squared number in a list
print(max(lst, key= lambda x: x*x))