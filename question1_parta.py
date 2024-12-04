def F(n):
    for j in range(n):
        str=""
        for i in range(2*n-1):
            if abs(n-i-1)<=j:
                str+=chr(65+abs(n-i-1))
            else:
                str+="-"
        print(str)
F(10)
F(6) 
                   