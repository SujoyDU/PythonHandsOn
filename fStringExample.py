class A():
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def __repr__(self):
        return(
            f"My name is {self.name}."
            f"I am {self.age} years old"
        ) 


name="Bob"
age = "18"

print(A(name,age))