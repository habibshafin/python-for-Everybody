def  computepay(h,r):
    if hours > 40 :
        pay = (rate * 40) + (1.5*rate*(hours - 40))
    else :
        pay = rate * hours
    return pay

hrs = input("Enter Hours:")
hours = int(hrs)
r = input("Enter rate:")
rate = float(r)

print('Pay',computepay(hours,rate))
