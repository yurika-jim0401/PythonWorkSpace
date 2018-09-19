def gen():
    for c in "AB":
        yield c


# list直接用生成器作为参数
print(list(gen()))


# yield from是一个中间层
def gen_new():
    yield from "AB"


print(list(gen_new()))
