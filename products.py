produscts = []
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':
		break
	price = input('請輸入價格: ')
	produscts.append([name, price])
print(produscts)

for p in produscts:
	print(p[0], '的價格是', p[1])