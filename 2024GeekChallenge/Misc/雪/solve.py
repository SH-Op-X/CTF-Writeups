with open("./demo/white.txt") as f:
    content = f.read()
print(content.encode())

from queue import LifoQueue
import re


stack = LifoQueue()

data = open("demo/white.txt", "r").read().splitlines()

"""
栈：后入先出
函数功能如下:
	push: 将数字压入栈顶
	printc: 将栈顶元素弹出并以ASCII字符形式输出
	dup: 复制栈顶元素后压入栈顶两次
	drop: 弹出栈顶元素
	add: 将堆栈最上方的两个元素弹出，二者做加法运算,得到的结果入栈
"""
text = ""
for line in data:
	if "push" in line:
		num = int(re.findall("push (.*?)$", line)[0])
		stack.put(num)
	elif line == "add":
		stack.put(stack.get() + stack.get())
	elif line == "dup":
		num = stack.get()
		stack.put(num)
		stack.put(num)
	elif line == "drop":
		asc = chr(stack.get())
		text += asc
print(text)
