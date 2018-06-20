'''
时间：2017年4月14日09:05:24
目的：引入外部Python文件
'''
#import mylib   第一种引入
#h = mylib.Hello()

from mylib import Hello   #第二种引入
h = Hello()

h.sayHello()

'''
运行结果：
	hello
'''