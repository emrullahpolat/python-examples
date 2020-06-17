def testDecorator(func):
    def inner(a,b):
        print("bu ilk metindir")
        func(a,b)
        print("bu son metindir")
    return inner

@testDecorator
def sayHello():
    print("merhabalar efendim")

@testDecorator
def sum(a,b):
    print(a+b)

#sayHello()
sum(4,5)