def mulComplex(a1,b1,a2,b2):
    # multiples (a1 + b1i)(a2 + b2i)
    return (a1*a2 - b1*b2, a1*b2 + a2*b1)

tempa, tempb = mulComplex(1,1,1,1)
for i in range(3, 1001):
    tempa, tempb = mulComplex(tempa, tempb, 1, 1)
    if i > 995:
        print(f"{i}, ({tempa}, {tempb})")