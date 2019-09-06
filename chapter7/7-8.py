sandwich_orders=['tuna','pastrami','tuna','pastrami','tuna','pastrami']
finished_sandwichs=[]
print(sandwich_orders)

while sandwich_orders:
 sandwich=sandwich_orders.pop()
 print("I made your "+sandwich+" sandwich.")
 finished_sandwichs.append(sandwich)

print(finished_sandwichs)
for finished_sandwich in finished_sandwichs:
 print(finished_sandwich)
