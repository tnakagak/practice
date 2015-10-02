# coding: utf-8
# 2分法

x = 25

epsilon = 0.01
low = 0.0
high = max(1.0, x)
ans = (low + high) / 2.0

while abs(ans ** 2 - x) > epsilon:
    print 'low is ', low , ' high is ', high , ' ans = ', ans

    if ans ** 2 < x:
        low = ans
    else:
        high = ans
    ans = (low + high) / 2.0

print ans , ' is close to square root of ' , x
