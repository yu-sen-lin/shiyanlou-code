for c in range(1,101):
    if c%7==0 or c%10==7 or c//10==7:
        continue
    print(c)
