name=input("Name:")
product=input('Product:')
price=int(input('Price per unit:$'))
units=int(input('Units:'))
subtotal= price * units
print(f'Name:{name}')
print(f'Product:{product}')
print(f'Price:{price}')
print(f"Units:{units}")
print(f'Subtotal:${subtotal}')
di=10/100
d=5/100
if subtotal>=100000:
    print(f"Discount:${subtotal*di}")
    print(f"Final price:${subtotal-(subtotal*di)}")
    print('You have received 10% discount.')
elif subtotal>=50000:
    print(f"Discount:${subtotal*d}")
    print(f"Final price:${subtotal-(subtotal*d)}")
    print("You received a 5%  discount.")
else:
    print('Discount:$0')
    print(f'Final price:${subtotal}')
    print('You receive no discount.')
