def testFunction(a: int):
    x = 0
    for i in range(5,a ** 2,2):
        for j in range(20,a,-3):
            x += 1
    return x

def testFunction2(x: list):
    z = 0
    for i in range(len(x)):
        z += 1
    return z
