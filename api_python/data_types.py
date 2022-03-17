from collections import OrderedDict

d = OrderedDict()
d["server"] = "mpilgrim"
d["database"] = "master"
d['mynewkey'] = 'mynewvalue'

print(d)

##Organiza os campos de forma crescente
orders = {
	'cappuccino': 54,
	'latte': 56,
	'espresso': 72,
	'americano': 48,
	'cortado': 41
}

sort_orders = sorted(orders.items(), key=lambda x: x[1])

for i in sort_orders:
	print(i[0], i[1])


##Organiza os campos de forma descrescente
orders = {
	'cappuccino': 54,
	'latte': 56,
	'espresso': 72,
	'americano': 48,
	'cortado': 41
}

sort_orders = sorted(orders.items(), key=lambda x: x[1], reverse=True)

for i in sort_orders:
	print(i[0], i[1])