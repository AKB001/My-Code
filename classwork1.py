class Check :
    def __init__(self,number) :
        self.num = number
    def isPrime(self) :
        for i in range(2, int(num ** (1/2)) + 1) :
            if num % i == 0 :
                return False
            return True

if __name__ == "__main__" :
    num = int(input("Enter the value:"))
    check_prime = Check(num)
    print(check_prime.isPrime())
    num = int(input("Enter the value:"))
    check_prime = Check(num)
    print(check_prime.isPrime()) 