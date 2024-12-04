r1 = int(input("enter the real  part of Z1: "))
i1 = int(input("enter the imaginary part of Z1: "))
Z1 = complex(r1, i1)

r2 = int(input("enter the real part of  Z2: "))
i2 = int(input("enter the imaginary part of Z2: "))
Z2 = complex(r2, i2)


Z = 1 / ((1 / Z1) + (1 / Z2))

print(f"Equivalent impedance : {Z}")
print(f"Z1 = {Z1}")
print(f"Z2 = {Z2}")

print(f"real part of Z equivalent : {Z.real}")
print(f"imaginary part of Z equivalent : {Z.imag}")