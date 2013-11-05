customer_1 ={"name":"lando","age":15}
customer_2 ={"name":"lando","age":15,"eyes":"brown"}
print customer_2
print customer_1
print type (customer_1)
print customer_1.keys()
print customer_1.values()
print customer_1.items()
print customer_1["name"]

if "eyes" in customer_2:
	print customer_2["eyes"]
else:
	print "no"