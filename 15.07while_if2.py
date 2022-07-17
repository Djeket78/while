
start=int(input('start: '))
end=int(input('end: '))

n=start

if start<end:
    while n<=end:
        print(n)
        n+=1
else:
    while n>=end:
        print(n)
        n-=1
                