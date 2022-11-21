def sayHelloTheUsualWay(name):
    print("Hello, World! - by", name)


if __name__ == "__main__":
    sayHello = lambda name: print("Hello,", name)
    sayHello("Ello Coder")
    sayHelloTheUsualWay("Ello Coder")


