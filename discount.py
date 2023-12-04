from datetime import date, timedelta, datetime

today = date.today()
print(today)

time = datetime.now()
print(time)

#tomorrow = today + 1
tomorrow = today + timedelta(days=1)
print(tomorrow)

print(time.hour)
print(today.day)

formated_date = datetime.now().strftime('%d/%m/%Y')
print(formated_date)

formated_time = datetime.now().strftime('%H:%M')
print(formated_time)

products = [
    {'sku': 1, 'exp_date': today, 'price': 100.0},
    {'sku': 2, 'exp_date': tomorrow, 'price': 50.0},
    {'sku': 3, 'exp_date': today, 'price': 200.0}
]

for product in products:
    # print(product)
    if product['exp_date'] != today:
        continue
    product['price'] *= 0.8
    print(F"""
    Price for sku {product['sku']}
    is now {product['price']}""")
