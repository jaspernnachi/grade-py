greet='Welcome to LTDPYTHON BMI calculator!'
customer_name = input('Enter your name: ')
print(f'{customer_name}! {greet}')
weight = float(input('Enter your weight in kilograms: '))
height = float(input('Enter your height in meters: '))
BMI = weight/height**2
print(f'Your weight is:.{weight}kg. Your height is:.{height}m.')
print(f'Your BMI is {BMI}.')

if BMI <= 0 or BMI >= 50:
    print('INVALID BMI FIGURE!')
elif BMI < 18.5:
    print(f'{customer_name}! You are Underweight!')
elif BMI <= 18.5 or BMI < 25:
    print(f'{customer_name}! Your weight is just Normal!')
elif BMI <= 25 or BMI < 30:
    print(f'{customer_name}! You are Overweight!')
elif BMI >= 30:
    print(f'{customer_name}! Oops You are obessed!')