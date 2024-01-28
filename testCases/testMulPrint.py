def testFunction(a: int):
    x = 0
    for i in range(5,a,3):
        for j in range(2,a,-3):
            x += 1
        print(x)
    return x

def testFunction2(x: list):
    z = 0
    for i in range(len(x)):
        z += 1
    return z
