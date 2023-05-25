def problem_1():

    # ADD TWO NUMBERS
    num1 = float(input("Enter your first number"))
    num2 = float(input("Enter your second number"))

    result = num1 + num2
    print("the sum of", num1, "and", num2, "is", result)


def problem_2():

    # GET Quotient of two numbers
    number1 = float(input("Enter your first number"))
    number2 = float(input("Enter your second number"))
    result = number1 / number2
    result2 = number1 // number2
    print("the quotient of", number1, "and", number2, "is", result)
    print("the quotient of", number1, "and", number2, "is", result2)


def problem_3():

    # GET quotient and division of two numbers
    numerator = 20
    denominator = 13

    quotient = numerator / denominator  # Using division operator (/)
    division = numerator // denominator  # Using floor division operator (//)

    print("Quotient:", quotient)
    print("Division:", division)


def problem_4():

    # input four numbers and generate the sum of these

    num1 = float(input("Enter your first number"))
    num2 = float(input("enter your second number"))
    num3 = float(input("enter your third number"))
    num4 = float(input("enter your fourth number"))

    sum_of_numbers = num1 + num2 + num3 + num4
    print("The sum of numbers are", sum_of_numbers)


def problem_5():

    # Sum and average of marks of five students taken from the user
    num_students = 5
    total_marks = 0


    for i in range(num_students):
        marks = float(input("Enter the marks of student {}: ".format(i + 1)))
        total_marks += marks

    average_marks = total_marks / num_students

    print("Sum of marks:", total_marks)
    print("Average marks:", average_marks)


def problem_6():

    # percentage of total marks of four
    num_students = 4
    max_marks = 100
    total_marks = 0

    # Input marks for each student
    for i in range(num_students):
        marks = float(input("Enter the marks of student {}: ".format(i + 1)))
        total_marks += marks

    percentage = (total_marks / max_marks) * 100
    # Calculate percentage
    # for i in range(num_students):
    #     marks = float(input("Enter the marks of student {}: ".format(i + 1)))
    #     percentage = (marks / max_marks) * 100
    #     print("Percentage of student {}: {:.2f}%".format(i + 1, percentage))


def problem_7():

    # check is number is greater than 80
    number = float(input("Enter a number"))
    if number > 80:
        print("Good")
    else:
        print("Try again")


def problem_8():

    # Get the number to check for divisibility
    number = int(input("Enter the number to check: "))

    # Get the number to divide by
    divisor = int(input("Enter the divisor: "))

    # Check for divisibility
    if number % divisor == 0:
        print(f"{number} is divisible by {divisor}.")
    else:
        print(f"{number} is not divisible by {divisor}.")


def problem_9():

    # Initialize a variable to hold the sum of odd numbers
    odd_sum = 0
    #fixme what if user enter odd number  ???

    # Get 10 numbers from the user
    for i in range(10):
        number = int(input(f"Enter number {i + 1}: "))

        # Check if the number is odd
        if number % 2 != 0:
            odd_sum += number

    # Print the sum of odd numbers
    print("Sum of odd numbers:", odd_sum)


def problem_10():
    # fixme what if user enter odd number  ???
    even_sum = 0

    # Get the value of n from the user
    n = int(input("Enter the value of n: "))

    # Get n numbers from the user
    for i in range(n):
        number = int(input(f"Enter number {i + 1}: "))

        # Check if the number is even
        if number % 2 == 0:
            even_sum += number

    # Print the sum of even numbers
    print("Sum of even numbers:", even_sum)


def problem_11():
    def fibonacci_series(n):
        series = [0, 1]  # Initialize the series with the first two terms

        for i in range(2, n):
            next_term = series[i - 1] + series[i - 2]
            series.append(next_term)

        return series[:n]  # Return only the first n terms

    # Example usage
    n = 10
    fibonacci_terms = fibonacci_series(n)
    print(fibonacci_terms)


def problem_12():
    # def fahrenheit_to_celsius(fahrenheit):
    fahrenheit = int(input("Enter fahrenheit :"))
    celsius = (fahrenheit - 32) * (5 / 9)
        # return celsius

    # Example usage

    # celsius = fahrenheit_to_celsius(fahrenheit)
    print(celsius)


def problem_13():
    def calculate_pay(hours_worked, rate_per_hour):
        if hours_worked <= 40:
            pay = hours_worked * rate_per_hour
        else:
            overtime_hours = hours_worked - 40
            overtime_rate = rate_per_hour * 1.5
            pay = (40 * rate_per_hour) + (overtime_hours * overtime_rate)
        return pay

    # Example usage
    hours = int(input("Enter work hours :"))
    rate = 10000
    total_pay = calculate_pay(hours, rate)
    print("Your total pay is ", total_pay, "PKR")


def problem_14():
    def determine_status(marks, passing_marks):
        if marks >= passing_marks:
            status = "Pass"
        else:
            status = "Fail"
        return status

    marks_obtained = int(input("Enter your marks :"))
    passing_marks = 50
    student_status = determine_status(marks_obtained, passing_marks)
    print(student_status)


def problem_15():

    def determine_largest_number(num1, num2):
        if num1 > num2:
            largest_num = num1
        else:
            largest_num = num2
        return largest_num

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    largest_number = determine_largest_number(num1, num2)
    print("The largest number is:", largest_number)


#take three numbers from the user and determine the largest
def problem_16():

    #fixme do it without max()
    def determine_largest_number(num1, num2, num3):
        largest_num = max(num1, num2, num3)
        return largest_num

    # Example usage
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    num3 = float(input("Enter the third number: "))
    largest_number = determine_largest_number(num1, num2, num3)
    print("The largest number is:", largest_number)


# using nested if-else
def problem_17():
    def determine_largest_number_nested(num1, num2, num3, num4):
        largest_num = num1

        if num2 > largest_num:
            largest_num = num2

        if num3 > largest_num:
            largest_num = num3

        if num4 > largest_num:
            largest_num = num4

        return largest_num

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    num3 = float(input("Enter the third number: "))
    num4 = float(input("Enter the third number: "))
    largest_number_nested = determine_largest_number_nested(num1, num2, num3, num4)
    print("Largest number using nested if-else:", largest_number_nested)


#using compound composition
def problem_18():
    #fixme do it without max()
        def determine_largest_number_compound(num1, num2, num3, num4):
            largest_num = max(num1, num2, num3, num4)
            return largest_num

        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        num3 = float(input("Enter the third number: "))
        num4 = float(input("Enter the third number: "))
        largest_number_compound = determine_largest_number_compound(num1, num2, num3, num4)
        print("Largest number using compound conditions:", largest_number_compound)


#using third approach
def problem_19():
    # Approach 3: Calling the first number the largest and revising estimate
    def determine_largest_number_estimate(num1, num2, num3, num4):
        largest_num = num1

        if num2 > largest_num:
            largest_num = num2

        if num3 > largest_num:
            largest_num = num3

        if num4 > largest_num:
            largest_num = num4

        return largest_num

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    num3 = float(input("Enter the third number: "))
    num4 = float(input("Enter the third number: "))
    largest_number_estimate = determine_largest_number_estimate(num1, num2, num3, num4)
    print("Largest number using estimation approach:", largest_number_estimate)


def problem_20():
    def calculate_grade(marks):
        if marks >= 90 and marks <= 100:
         return "A"
        elif marks >= 80 and marks <= 89:
         return "B"
        elif marks >= 70 and marks <= 79:
         return "C"
        elif marks >= 60 and marks <= 69:
         return "D"
        else:
         return "F"

    student_marks = float(input("Enter your marks :"))
    student_grade = calculate_grade(student_marks)
    print("Student Grade:", student_grade)


def problem_21():
    #fixme what if user enter 0 ?
    def check_even_odd(number):
        if number % 2 == 0:
            return "Even"
        else:
            return "Odd"

    # Example usage:
    user_number = int(input("Enter a number: "))
    result = check_even_odd(user_number)
    print("The number is", result)


def problem_22():
    from datetime import datetime, timedelta

    def calculate_time_difference(time1, time2):
        fmt = '%H:%M'
        datetime1 = datetime.strptime(time1, fmt)
        datetime2 = datetime.strptime(time2, fmt)
        difference = datetime2 - datetime1
        return difference

    time1 = "10:15"
    time2 = "13:45"

    time_difference = calculate_time_difference(time1, time2)
    print("Time difference:", time_difference)


def problem_23():
    def check_numbers(a, b, c):
        if a == b == c:
            return "All numbers are the same"
        elif a != b and b != c and a != c:
            return "All numbers are different"
        else:
            return "Exactly two numbers are the same"

    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    num3 = int(input("Enter the third number: "))
    result = check_numbers(num1, num2, num3)
    print(result)


def problem_24():
    sum = 0

    for i in range(10):
        num = float(input("Enter number {}: ".format(i + 1)))
        sum += num
    print("The sum of the 10 numbers is:", sum)


def problem_25():
    n = int(input("Enter the count of numbers: "))
    sum = 0

    for i in range(n):
        num = float(input("Enter number {}: ".format(i + 1)))
        sum += num
    print("The sum of the", n, "numbers is:", sum)


def problem_26():
    n = int(input("Enter the count of numbers: "))
    sum = 0
    for i in range(n):
        num = float(input("Enter number {}: ".format(i + 1)))
        sum += num
    average = sum / n
    print("The average of the", n, "numbers is:", average)


def problem_27():
    n = int(input("Enter a number: "))
    for i in range(1, n + 1):
        print(i)


def problem_28():
    n = int(input("Enter a positive integer: "))
    factorial = 0
    if n < 0:
        print("Error: Please enter a positive integer.")
    elif n == 0:
        factorial = 1
    else:
        factorial = 1
        for i in range(1, n + 1):
            factorial *= i

    print("The factorial of", n, "is", factorial)


def problem_29():
    a = int(input("Enter the value of 'a': "))
    n = int(input("Enter the value of 'n': "))

    result = 1
    for _ in range(n):
        result *= a

    print(f"The result of {a} raised to the power of {n} is: {result}")


def problem_30():
    numbers = []

    for i in range(3):
        num = int(input(f"Enter number {i + 1}: "))
        numbers.append(num)

    largest = numbers[0]

    for num in numbers:
        if num > largest:
            largest = num

    print(f"The largest number is: {largest}")


def problem_31():
    n = int(input("Enter a value of n :"))
    numbers = []

    for i in range(n):
        num = int(input(f"Enter number {i + 1}: "))
        numbers.append(num)

    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    print(f"The largest number is: {largest}")


def problem_32():
    n = int(input("Enter the value of 'n': "))

    numbers = []

    for i in range(n):
        num = int(input(f"Enter number {i + 1}: "))
        numbers.append(num)

    # numbers.sort()
    # numbers[0]
    # numbers[-1]
    smallest = numbers[0]
    largest = numbers[0]
    for num in numbers:
        if num < smallest:
            smallest = num
        if num > largest:
            largest = num

    print(f"The smallest number is: {smallest}")
    print(f"The largest number is: {largest}")


#Take n numbers from the user and determine that how many positive and negative
def problem_33():
    n = int(input("Enter the value of 'n': "))

    positive_count = 0
    negative_count = 0

    for i in range(n):
        num = int(input(f"Enter number {i + 1}: "))
        if num > 0:
            positive_count += 1
        elif num < 0:
            negative_count += 1

    print(f"Number of positive integers: {positive_count}")
    print(f"Number of negative integers: {negative_count}")



#Take a positive integer n from the user. Display all the divisors of n
def problem_34():
    n = int(input("Enter a positive integer: "))

    divisors = []

    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)

    print(f"The divisors of {n} are: {divisors}")


#input a positive integer from the user and determine where the number is a perfect
def problem_35():
    n = int(input("Enter a positive integer: "))

    divisors_sum = 0

    for i in range(1, n):
        if n % i == 0:
            divisors_sum += i

    if divisors_sum == n:
        print(f"{n} is a perfect number.")
    else:
        print(f"{n} is not a perfect number.")


#Input a positive integer from the user and determine whether is a prime number or
def problem_36():
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    num = int(input("Enter a positive integer: "))
    if is_prime(num):
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")


# Take a positive integer from the user. Displaying an error message and prompting
# for input again and again if the user enters invalid input (negative or zero)
def problem_37():
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    while True:
        num = int(input("Enter a positive integer: "))
        if num <= 0:
            print("Invalid input. Please enter a positive integer.")
        else:
            break

    if is_prime(num):
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")


# Write an algorithm to determine the sum of a variable number of positive integers taken from the user. The algorithm should keep prompting the user for more input
# until the user enters the sentinel value -999.
def problem_38():
    total = 0
    num = 0

    while num != -999:
        num = int(input("Enter a positive integer or -999 to terminate: "))
        if num > 0:
            total += num

    print("The sum of the positive integers is:", total)


# Display negative of a number
def problem_39():
    # Get input from the user
    num = float(input("Enter a number: "))

    # Calculate the negative of the number
    negative_num = -1 * num

    # Display the negative number
    print("The negative of", num, "is", negative_num)


#  Find absolute of an input. Assume that the absolute operator is not available
def problem_40():
    # Get input from the user
    num = float(input("Enter a number: "))

    # Calculate the absolute value of the number
    absolute_num = num if num >= 0 else -num

    # Display the absolute value
    print("The absolute value of", num, "is", absolute_num)


# input 2 number and find if both are even, both are odd, or 1 even 1 odd.
def problem_41():
    # Get input from the user
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    # Check if both numbers are even, both odd, or one even and one odd
    if num1 % 2 == 0 and num2 % 2 == 0:
        print("Both numbers are even.")
    elif num1 % 2 != 0 and num2 % 2 != 0:
        print("Both numbers are odd.")
    else:
        print("One number is even and the other is odd.")


# Input 3 numbers and find how many are odd.
def problem_42():
    # Get input from the user
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    num3 = int(input("Enter the third number: "))
    odd_count = 0
    if num1 % 2 != 0:
        odd_count += 1
    if num2 % 2 != 0:
        odd_count += 1
    if num3 % 2 != 0:
        odd_count += 1
    print("The number of odd numbers is:", odd_count)


# Input 3 numbers and print the 2 largest numbers
def problem_43():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    num3 = int(input("Enter the third number: "))
    largest = max(num1, num2, num3)
    smallest = min(num1, num2, num3)
    second_largest = num1 + num2 + num3 - largest - smallest
    print("The two largest numbers are:", largest, "and", second_largest)


# Input a number and find if it is 2-digit positive integer or not
def problem_44():
    # Get input from the user
    num = int(input("Enter a number: "))

    # Check if the number is a 2-digit positive integer
    if 10 <= num <= 99:
        print("The number is a 2-digit positive integer.")
    else:
        print("The number is not a 2-digit positive integer.")


# Input a 2-digit number and find the absolute difference between its digits
def problem_45():
    number = int(input("Enter a 2-digit number: "))
    tens_digit = number // 10
    units_digit = number % 10
    absolute_difference = abs(tens_digit - units_digit)
    print("Absolute difference between the digits:", absolute_difference)


# Input an integer (up to 4 digits) and store its reverse in another variable. Then
# display both integers.
def problem_46():
    number = int(input("Enter an integer (up to 4 digits): "))
    reverse_number = int(str(number)[::-1])
    print("Original number:", number)
    print("Reversed number:", reverse_number)


# Interchange two numbers
def problem_47():
    a = int(input("Enter the first number (a): "))
    b = int(input("Enter the second number (b): "))

    print("Before interchange: a =", a, "b =", b)

    temp = a
    a = b
    b = temp

    print("After interchange: a =", a, "b =", b)


# Interchange two numbers without using an extra variable.
def problem_48():
    a = int(input("Enter the first number (a): "))
    b = int(input("Enter the second number (b): "))

    print("Before interchange: a =", a, "b =", b)

    a = a + b
    b = a - b
    a = a - b

    print("After interchange: a =", a, "b =", b)


# Multiply a number with the sum of its digits
def problem_49():
    number = int(input("Enter a number: "))

    # Calculate the sum of digits
    digit_sum = sum(int(digit) for digit in str(number))

    # Multiply the number with the sum of digits
    result = number * digit_sum

    print("Result:", result)


# Conversion of microseconds to weeks, days, hours, minutes, seconds, and
# remaining microseconds.
def problem_50():
    microseconds = int(input("Enter the number of microseconds: "))
    weeks = microseconds // (7 * 24 * 60 * 60 * 1000000)
    microseconds %= 7 * 24 * 60 * 60 * 1000000
    days = microseconds // (24 * 60 * 60 * 1000000)
    microseconds %= 24 * 60 * 60 * 1000000
    hours = microseconds // (60 * 60 * 1000000)
    microseconds %= 60 * 60 * 1000000
    minutes = microseconds // (60 * 1000000)
    microseconds %= 60 * 1000000
    seconds = microseconds // 1000000
    microseconds %= 1000000

    print("Weeks:", weeks)
    print("Days:", days)
    print("Hours:", hours)
    print("Minutes:", minutes)
    print("Seconds:", seconds)
    print("Microseconds:", microseconds)


# Input 2 numbers and print YES if 1st is divisible by 2nd
def problem_51():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    if num1 % num2 == 0:
        print("YES")
    else:
        print("NO")


# Input 2 numbers and print YES if 2nd is divisible by 1st
def problem_52():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    if num2 % num1 == 0:
        print("YES")
    else:
        print("NO")


# Input 2 numbers and print YES if one number is divisible by the other
def problem_53():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    if num1 % num2 == 0 or num2 % num1 == 0:
        print("YES")
    else:
        print("NO")


# Input numbers till user inputs a zero and display their sum.
def problem_54():
    numbers = []
    num = int(input("Enter a number (or 0 to stop): "))

    while num != 0:
        numbers.append(num)
        num = int(input("Enter a number (or 0 to stop): "))

    total = sum(numbers)
    print("Sum of the numbers:", total)


# Input numbers till user inputs a zero and at the end display last non-zero number
def problem_55():
    last_non_zero = 0
    num = int(input("Enter a number (or 0 to stop): "))

    while num != 0:
        last_non_zero = num
        num = int(input("Enter a number (or 0 to stop): "))

    print("Last non-zero number:", last_non_zero)


# Input numbers till user inputs a zero and display the largest number
def problem_56():
    numbers = []
    num = int(input("Enter a number (or 0 to stop): "))

    while num != 0:
        numbers.append(num)
        num = int(input("Enter a number (or 0 to stop): "))

    if numbers:
        max_num = max(numbers)
        print("Largest number:", max_num)
    else:
        print("No numbers were entered.")


# Input numbers till user inputs a zero, and display the smallest number
def problem_57():
    numbers = []
    num = int(input("Enter a number (or 0 to stop): "))

    while num != 0:
        numbers.append(num)
        num = int(input("Enter a number (or 0 to stop): "))

    if numbers:
        min_num = min(numbers)
        print("Smallest number:", min_num)
    else:
        print("No numbers were entered.")


# input numbers till user inputs a zero and display the largest number
def problem_58():
    numbers = []
    num = int(input("Enter a number (or 0 to stop): "))

    while num != 0:
        numbers.append(num)
        num = int(input("Enter a number (or 0 to stop): "))

    if numbers:
        max_num = float('-inf')  # Set initial value to smallest possible negative number
        for num in numbers:
            if num > max_num:
                max_num = num
        print("Largest number:", max_num)
    else:
        print("No numbers were entered.")


# Input 10 numbers, and display the smallest number
def problem_59():
    numbers = []
    for _ in range(10):
        num = int(input("Enter a number: "))
        numbers.append(num)

    min_num = min(numbers)
    print("Smallest number:", min_num)


# Input 10 numbers, and display count of even and odd numbers, separately, at the
# end
def problem_60():
    even_count = 0
    odd_count = 0

    for _ in range(10):
        num = int(input("Enter a number: "))
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    print("Count of even numbers:", even_count)
    print("Count of odd numbers:", odd_count)


# Input SLimit and elimit from the user, and display even numbers between range,
# with both limit, included.
def problem_61():
    slimit = int(input("Enter the starting limit: "))
    elimit = int(input("Enter the ending limit: "))

    # Adjust the starting limit to the next even number if it's odd
    if slimit % 2 != 0:
        slimit += 1

    # Iterate from starting limit to ending limit (inclusive) with a step of 2
    for num in range(slimit, elimit + 1, 2):
        print(num)


#  Input SLimit and ELimit from the user and display only those numbers between
# range which are divisible by 2 or 3 or 5, with both limits include
def problem_62():
    slimit = int(input("Enter the starting limit: "))
    elimit = int(input("Enter the ending limit: "))

    for num in range(slimit, elimit + 1):
        if num % 2 == 0 or num % 3 == 0 or num % 5 == 0:
            print(num)


# Input 2 numbers and find their GCD
def problem_63():
    import math

    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    gcd = math.gcd(num1, num2)
    print("GCD:", gcd)


# Input 2 numbers and display their LCM.
def problem_64():
    import math

    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    lcm = abs(num1 * num2) // math.gcd(num1, num2)
    print("LCM:", lcm)


#  Input a number and display that how many digits it has.
def problem_65():
    number = input("Enter a number: ")
    digit_count = len(number)
    print("The number has", digit_count, "digit(s).")


# Input two positive integers a and b from the user. Determine the remainder of a/b.
# Assume that the division and modulus operators are not available.
def problem_66():
    def calculate_remainder(a, b):
        while a >= b:
            a -= b
        return a
    a = int(input("Enter the value of a: "))
    b = int(input("Enter the value of b: "))

    remainder = calculate_remainder(a, b)
    print("The remainder of", a, "divided by", b, "is", remainder)


# Input two positive integers and a and b from the user. Determine the integer of a/b.
# Assume that the division operator is not available
def problem_67():
    # Read input values
    a = int(input("Enter the value of a: "))
    b = int(input("Enter the value of b: "))

    # Initialize variables
    quotient = 0

    # Perform repeated subtraction to calculate integer division
    while a >= b:
        a -= b
        quotient += 1

    # Output the integer division result
    print("Integer division result (a/b):", quotient)


def problem_68():
    # Read input values
    a = int(input("Enter the value of a: "))
    b = int(input("Enter the value of b: "))

    # Initialize variables
    remainder = a

    # Perform repeated subtraction to calculate the remainder
    while remainder >= b:
        remainder -= b

    # Output the remainder
    print("Remainder (a%b):", remainder)


# Input a base-9 number, digit by digit, then convert it into decimal number. Digits of
# the input will be entered in order from least significant to most significant. Since
# valid digits are 0 to 8, hence any other input will be used as the sentinel value.
def problem_69():
    def base9_to_decimal():
        base9_number = []

        while True:
            digit = input("Enter a digit (0-8) of the base-9 number (Enter any other value to stop): ")

            if digit.isdigit() and int(digit) in range(9):
                base9_number.append(int(digit))
            else:
                break

        decimal_number = 0
        power = 0

        for digit in base9_number:
            decimal_number += digit * (9 ** power)
            power += 1

        return decimal_number

    # Example usage
    decimal = base9_to_decimal()
    print("Decimal number:", decimal)


# Input a base-9 number, digit by digit, then convert it into decimal number. Digits of
# the input will be entered in order from most significant to least significant. Since
# valid digits are 0 to 8, hence any other input will be used as sentinel value.
def problem_70():
    def base9_to_decimal():
        base9_number = []

        while True:
            digit = input("Enter a digit (0-8) of the base-9 number (Enter any other value to stop): ")

            if digit.isdigit() and int(digit) in range(9):
                base9_number.insert(0, int(digit))
            else:
                break

        decimal_number = 0
        power = 0

        for digit in base9_number:
            decimal_number += digit * (9 ** power)
            power += 1

        return decimal_number

    # Example usage
    decimal = base9_to_decimal()
    print("Decimal number:", decimal)


def problem_71():
    def decimal_to_base9(decimal_number):
        base9_digits = []

        while decimal_number > 0:
            remainder = decimal_number % 9
            base9_digits.insert(0, remainder)
            decimal_number //= 9

        for digit in base9_digits:
            print(digit)

    decimal = int(input("Enter a decimal number: "))
    print("Base-9 representation:")
    decimal_to_base9(decimal)


# Input a base-9 number, digit by digit, then convert it into decimal number. Digits of
# the input will be entered in order from least significant to most significant. Since
# valid digits are 0 to 8, hence any other input will be used as the sentinel value.
def problem_72():
    def decimal_to_base9(decimal_number):
        base9_value = 0
        power = 0

        while decimal_number > 0:
            remainder = decimal_number % 9
            base9_value += remainder * (10 ** power)
            decimal_number //= 9
            power += 1

        return base9_value

    # Example usage
    decimal = int(input("Enter a decimal number: "))
    base9 = decimal_to_base9(decimal)
    print("Base-9 representation:", base9)


# Input a decimal integer and display its hexadecimal equivalent digit-by-digit. The
# hexadecimal output should be in order from least significant to most significan
def problem_73():
    def decimal_to_hex(decimal_number):
        hex_digits = []

        while decimal_number > 0:
            remainder = decimal_number % 16
            hex_digits.append(remainder)
            decimal_number //= 16

        hex_digits.reverse()

        for digit in hex_digits:
            hex_digit = hex(digit)[2:]
            print(hex_digit.upper())

    # Example usage
    decimal = int(input("Enter a decimal number: "))
    print("Hexadecimal representation (least significant to most significant):")
    decimal_to_hex(decimal)


# three numbers denoted by the variables A, B and C are supplied as input data. Print
# these three number in ascending order.
def problem_74():
    A = float(input("Enter the value for A: "))
    B = float(input("Enter the value for B: "))
    C = float(input("Enter the value for C: "))

    # Sort the numbers in ascending order
    numbers = [A, B, C]
    numbers.sort()

    # Print the sorted numbers
    print("The numbers in ascending order are:", numbers[0], numbers[1], numbers[2])


if __name__ == "__main__":

    # problem_1()
    # problem_2()
    # problem_3()
    # problem_4()
    # problem_5()
    # problem_6()
    # problem_7()
    # problem_8()
    # problem_9()
    # problem_10()
    # problem_11()
    # problem_12()
    # problem_13()
    # problem_14()
    # problem_15()
    # problem_16()
    # problem_17()
    # problem_18()
    # problem_19()
    # problem_20()
    # problem_21()
    # problem_22()
    # problem_23()
    # problem_24()
    # problem_25()
    # problem_26()
    # problem_27()
    # problem_28()
    # problem_29()
    # problem_30()
    # problem_31()
    # problem_32()
    # problem_33()
    # problem_34()
    # problem_35()
    # problem_36()
    # problem_37()
    # problem_38()
    # problem_39()
    # problem_41()
    # problem_42()
    # problem_43()
    # problem_44()
    # problem_45()
    # problem_46()
    # problem_47()
    # problem_48()
    # problem_49()
    # problem_50()
    # problem_51()
    # problem_52()
    # problem_53()
    # problem_54()
    # problem_55()
    # problem_56()
    # problem_57()
    # problem_58()
    # problem_59()
    # problem_60()
    # problem_61()
    # problem_62()
    # problem_63()
    # problem_64()
    # problem_65()
    # problem_66()
    # problem_67()
    # problem_68()
    # problem_69()
    # problem_70()
    # problem_71()
    # problem_72()
    # problem_73()
    problem_74()



