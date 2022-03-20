from collections import OrderedDict

def orderdict():

	d = OrderedDict()
	d["server"] = "mpilgrim"
	d["database"] = "master"
	d['mynewkey'] = 'mynewvalue'

	print(d)

orderdict()

def organizar_crescente_desc():

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

def insert_quote_in_dict():

	data = {
		"topic": "kafka_topic",
		"flush_size": 1000,
		"schema": "backward",
		"message_size": 200,
		"branch": "develop"
	}

	var = data.get('message_size')
	print(var)

insert_quote_in_dict()