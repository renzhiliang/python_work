sandwich_orders=['tuna','pastrami','tuna','pastrami','tuna','pastrami']
print(sandwich_orders)

#while 'pastrami' in sandwich_orders:
# sandwich_orders.remove('pastrami')

for sandwich_order in sandwich_orders:
 if sandwich_order=='pastrami':
  sandwich_orders.remove('pastrami')

print(sandwich_orders)
