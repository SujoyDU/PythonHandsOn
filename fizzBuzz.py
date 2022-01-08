#all integers divided by 3 fizz
#all integers divided by 5 buzz
#all integers divided by 3 and 5 FizzBuzz

def fizz_buzz_range(numbers):

    for i in range(0,len(numbers)):
        if(numbers[i]%3==0 and numbers[i]%5==0): 
            print("FizzBuzz")
            numbers[i]="FizzBuzz"
        elif(numbers[i]%3 == 0): 
            print("fizz")
            numbers[i]="fizz"

        elif(numbers[i]%5 == 0): 
            print("buzz")
            numbers[i]="buzz"
        else: print(numbers[i])
    
    return

def fizz_buzz_enumerate(numbers):

    print("enumearte:")
    for (k,i) in enumerate(numbers):
        if(i%3==0 and i%5==0): 
            print("FizzBuzz")
            numbers[k]="FizzBuzz"
        elif(i%3 == 0): 
            print("fizz")
            numbers[k]="fizz"
        elif(i%5 == 0): 
            print("buzz")
            numbers[k]="buzz"
        else: print(i)
    
    return 

numbers1=[3,6,9,10,15,20,21,25,30,27,29,4]
numbers2=[3,6,9,10,15,20,21,25,30,27,29,4]
fizz_buzz_range(numbers1)
fizz_buzz_enumerate(numbers2)
print(numbers1)
print(numbers2)