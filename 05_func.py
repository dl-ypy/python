'''
时间：2017年4月14日08:45:00
目的：函数
'''
#无参
def sayHello():
	print("hello")

#调用无参函数
sayHello()

#有参
def max(a,b):
	if a>b:
		print(a)
	else:
		print(b)

#调用有参函数
max(2,5)
'''
运行结果：
	hello
	5
'''