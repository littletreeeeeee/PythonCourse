from decimal import Decimal as Dec

print Dec(2.968)
print Dec('2.968')
print Dec(0.001)*Dec(2968)-Dec(2.968)
print Dec('0.001')*Dec(2968)-Dec('2.968')