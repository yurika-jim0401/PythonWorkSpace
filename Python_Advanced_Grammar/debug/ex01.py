def SayHello(name):
    print("hello,{0}".format(name))
    print("bye bye")

if __name__ == "__main__":
    print('***'*10)
    name = input("plz input your name:")
    print(SayHello(name))
    print('@@@'*10)