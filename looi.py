X11 =int(input())
Y11 = []
Z11 = ['a','e','i','o','u']
A=0
for P in range(0,X11):
    Y11.append(list(input()))

    for E in Y11[i]:
        if E in Z11:
            A = A+1
            break

if A == X11:
    print("yes")
else:
    print("no")
