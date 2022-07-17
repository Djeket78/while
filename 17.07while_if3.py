

start=int(input('start: '))
end=int(input('end: '))

n=start

while True:
    print(n)

    if n==end:
        break
    if start<end:
        n+=1
    else:
        n-=1
                    