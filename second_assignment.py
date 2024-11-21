greet = 'Welcome to LTDPYTHON TRIANGLE CHECKER!'
name = input('Enter your name: ')
side_1 = float(input('Enter the length of the FIRST side: '))
side_2 = float(input('Enter the length of the SECOND side: '))
side_3 = float(input('Enter the length of the THIRD side: '))

            # i used inequility theorem
if side_1 + side_2 <= side_3 or side_1 + side_3 <= side_2 or side_2 + side_3 <= side_1:
    print('Invalid triangle length!')

if side_1 == side_2 == side_3:
    print('The triangle is equilateral.')
elif side_1 == side_2 or side_2 == side_3 or side_1 == side_3:
    print('The triangle is Isosceles.')
elif side_1 != side_2 or side_2 != side_3 or side_1 != side_3:
    print('This is a scalene Trianle.')

    if side_1 + side_2 + side_3 >= 181:
        print('Oops!, INVALID TRIAGLE SIDES!')