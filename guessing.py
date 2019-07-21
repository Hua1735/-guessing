import random
r = random.randint(1, 100)
while True :
	g = input('請猜一個整數數字: ')
	g = int(g)
	if g == r:
		print('答對了')
		break
	if g >= r:
		print('太大了,再猜一次')
	if g <= r:
		print('太小了，再猜一次')
