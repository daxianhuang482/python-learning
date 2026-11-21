# hello.py —— 我的第一个 Python 程序
# 运行方式：在终端输入  python hello.py

print("Hello, World!")
print("你好，欢迎开始学 Python！")

# 变量：给数据起个名字
name = "同学"
days = 30

print(f"{name}，你计划用 {days} 天打好基础。")

# 循环：让计算机重复干活
for i in range(1, 6):
    print(f"{i} 的平方是 {i ** 2}")

# 函数：把一段逻辑打包起来，随时调用
def greet(who):
    return f"加油，{who}！"

print(greet(name))
print("这次真的改动了，能看到吗？")
