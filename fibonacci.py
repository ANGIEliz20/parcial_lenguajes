

#create a class for the methods
class ClaseDeJhonatan:

    #define method called fibonacci
        def Fibonacci(self,n):
            
            #define 2 variables, a and b. 
            #fibonacci start in 0 and 1 but in this excercise initialize in 1 and 1 because we need start in 1
            a,b = 1,1
            
            #this loop repeat n times
            for i in range (n):

                #print a in his first value
                print(f"Your fibonacci loop success in: {a}")

                #the value of b is for a then a plus b is for b
                a,b = b, a + b

                #repeat this loop

#Create a instance of the class called parcial 
parcial = ClaseDeJhonatan()

serieInput = int(input("Enter the times for your loop code: "))
#call the fibonacci method in parcial
parcial.Fibonacci(serieInput)

