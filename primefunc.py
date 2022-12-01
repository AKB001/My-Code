def prime():
    num = int(input("Enter a number: "))
    counter=0
    if num >= 1:
    
        
   
        for i in range(2,num):
            
            if (num % i) == 0:
                counter+=1
                break
            
                
    else:
        print(num,"is a prime number")
    if(counter>0):
        print("The number is not prime ",num)
prime()