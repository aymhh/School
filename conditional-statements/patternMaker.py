sign = "*"

while len(sign) < 5:
    print(sign)
    sign += '*'

while len(sign) >= 1:
    print(sign)
    sign = sign[:-1]