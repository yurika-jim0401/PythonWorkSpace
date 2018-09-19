# pickle实例
import pickle
# shelve案例
import shelve
age = 19
name = "jim"

# 序列化案例
with open(r"F:\PythonWorkSpace\pest2.txt", 'wb') as f:
    # 将age的19落地
    # 最后一个参数为0时,表示用ASCII协议
    pickle.dump(age, f, 0)
    pickle.dump(name, f, 0)

# 反序列化案例
with open(r"F:\PythonWorkSpace\pest2.txt", 'rb') as f:
    # 将age的19落地
    # 最后一个参数为0时,表示用ASCII协议
    age1 = pickle.load(f)
    name1 = pickle.load(f)
    print(age1, name1)

# 复杂点的序列化案例
l = [19, 'jim', 'i love yyt', [165, 57]]
with open(r"F:\PythonWorkSpace\pest2.txt", 'wb') as f:
    # 将age的19落地
    # 最后一个参数为0时,表示用ASCII协议
    pickle.dump(l, f, 0)
with open(r"F:\PythonWorkSpace\pest2.txt", 'rb') as f:
    # 将age的19落地
    # 最后一个参数为0时,表示用ASCII协议
    a1 = pickle.load(f)
    print(a1)

# 使用shelve创建文件并使用
# 打开一个文件,这里的shv相当于一个字典
shv = shelve.open(r"F:\PythonWorkSpace\shv.db")
shv['one'] = 1
shv['two'] = 2
shv['three'] = 3
shv.close()
# 通过以上案例发现,shelve自动建立的不仅仅是一个shv.db文件,还包括其他格式文件

# shelve读取
shv = shelve.open(r"F:\PythonWorkSpace\shv.db")
try:
    print(shv['one'])
    # 当出现字典中不存在的key时,要用异常,不然会保存
    print(shv['threeee'])
except Exception as e:
    print("没有这个")
finally:
    # 将close放在finally中,无论发生什么,总会执行close
    shv.close()

# shelve之 只读打开
shv = shelve.open(r"F:\PythonWorkSpace\shv.db", flag='r')
try:
    k1 = shv['one']
    print(k1)
finally:
    shv.close()

# shelve忘记写回,需要使用强制写回 writeback= True)
shv = shelve.open(r"F:\PythonWorkSpace\shv.db", writeback=True)
try:
    k1 = shv['one']
    print(k1)
    # 此时,一旦shelve关闭,则内容还是存在内存中,并没有写入数据
    shv['one'] = 100
finally:
    shv.close()

# shelve 使用with管理上下文环境
with shelve.open(r"F:\PythonWorkSpace\shv.db", writeback=True) as shv:
    k1 = shv['one']
    print(k1)
    shv['one'] = 1000
with shelve.open(r"F:\PythonWorkSpace\shv.db") as shv:
    print(shv['one'])

