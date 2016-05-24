def digit_sum(n):
    dsum = 0
    while n>0:
        dsum += n%10
        print dsum
        n/=10
    return dsum
print digit_sum(1234)
