import random
r = random.randint(1, 100)
count = 0
while True :
	count += 1
	g = input('請猜一個整數數字: ')
	g = int(g)
	if g == r:
		print('答對了')
		break
	elif g >= r:
		print('太大了,再猜一次')
	elif g <= r:
		print('太小了，再猜一次')
	print('總共猜了', count, '次')
