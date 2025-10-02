def farenheit_to_celsius(farenheit):
    celsuis=(5/9)*(farenheit-32)
    return celsuis

f=75
c=farenheit_to_celsius(f)

print(f"{f}F={c:.2f}C" )