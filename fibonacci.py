


#Implement a Fibonacci series generator


nterms =int(input('How Many Term: '))
n1=0
n2=1
count=0

if nterms <= 0:
    print("Please enter a positive integer")
elif nterms == 1:
    print("fibonacci sequence upto",nterms, ":")
    print(n1)
else:
    print("fibonacci sequence: ")
    while count < nterms:
        print(n1)

        nth =n1+n2
        n1 = n2
        n2 = nth
        count += 1



