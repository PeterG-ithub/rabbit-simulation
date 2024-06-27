def lerp(a, b, t):  # lerp(PL, PU, t) where: PL = lower probability, PU = Upper Probablity
    num = (b + t * (a - b))
    num = round(num, 2)
    if num < a:
        num = a
    elif num > b:
        num = b
    return num
