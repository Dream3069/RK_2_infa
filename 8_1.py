a = "101101"
b = "110011"

a_int = int(a, 2)
b_int = int(b, 2)

and_result = bin(a_int & b_int)[2:]
sum_result = bin(a_int + b_int)[2:]

print(f"Побитовое AND ({a}, {b}): {and_result}")
print(f"Сумма ({a}, {b}): {sum_result}")