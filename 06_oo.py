'''
时间：2017年4月14日08:54:28
目的：面向对象
'''
#父类
class Hello:
	def __init__(self,name):   #构造函数
		self._name = name
	
	def sayHello(self):
		print("Hello {0}".format(self._name))
		
#子类继承父类
class Hi(Hello):
	def __init__(self,name):
		Hello.__init__(self,name)    #必须先调用父类的构造方法
		
	def sayHi(self):
		print("Hi {0}".format(self._name))

h = Hello("ypy")  #创建对象
h.sayHello()
h1 = Hi("q")
h1.sayHi()
'''
运行结果：
	Hello ypy
	Hi q
'''