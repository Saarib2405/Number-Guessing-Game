import random
a=random.randint(1,10)
while a>0:
    option=int(input("Choices\n1.Continue Game\n2.End Game\nEnter your Choice: "))
    
    while option==1:
        #attempts=0
        def guess():
            num=int(input("Enter a number: "))
            
            if num==a:
                print("You guesssed the number!!")
                exit()
            elif num>a:
                print("Guessed Number is high")
            elif num<a:
                print("Guessed Number is low")
            else:
                print("Enter correct number")
            #attempts=attempts+1      
        guess()
        #print(attempts)
        break
    else:
        if option==2:
            print("Thank You")
            exit()
        else:
            print("Enter the correct choice")
        

     

