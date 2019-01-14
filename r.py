#产生一个randint 即随机整数（不打印）
#请使用者重复输入数字猜
#猜对的话 印出“终于猜对了”
#猜错的话 印出 比答案大/小

import random

#（.是“的”的意思）从random中的1-100取随机整数，再存进r
r = random.randint(1,100)
#count=0写在while true上面才不会每次都循环归零
count = 0
while True:
#count+1需要循环，所以放在while true的block里
#count += 1是“count = count +1”的缩写
	count += 1
	num = input('please guess the number：')
#input会自动存成字串，一定要casting
#因为已经设置为int，所以输入非数字的内容都会invalid当机
	num = int(num)
#num是对方输入的数字，r是自己设置的数字
	if num == r:
		print('Yeah!')
#这里要写“猜了几次”的命令，否则break的话逃出loop就不打印猜了几次了
		print('its your', count ,'time')
		break
	elif num > r:
		print('too big')
	elif num < r:
		print('too small')
#“猜了几次”写在if架构下一行，这样就不用写三次了（if后，elif后，elif后）
	print('its your', count ,'time')



	

