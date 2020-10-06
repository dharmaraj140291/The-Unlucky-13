for _ in range(int(input())):
        n=int(input())
        c=[str(i).zfill(n) for i in range(0,pow(10,n))]
        count=0
        for i in c:
             if "13" in i:
                pass
             else:
                count+=1   
        print(count)
