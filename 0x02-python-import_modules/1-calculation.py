#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div

a = 10
b = 5
add_sum = add(a, b)
sub_sum = sub(a, b)
mul_sum = mul(a, b)
div_sum = div(a, b)
print("{} + {} = {}".format(a, b, add_sum))
print("{} - {} = {}".format(a, b, sub_sum))
print("{} * {} = {}".format(a, b, mul_sum))
print("{} / {} = {}".format(a, b, div_sum))
