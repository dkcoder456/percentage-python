# gives output of the second numberin the percentage of the first number and the percentage given by the user
def calculate_second_number():
    print("Number and Percentage Calculator")
    print("--------------------------------")
    
    print("Enter the first number:")
    first_number = float(input())
    
    print("Enter the percentage:")
    percentage = float(input())
    
    # Calculate second number
    second_number = (first_number * percentage) / 100
    
    print(f"\nResults:")
    print(f"First Number: {first_number}")
    print(f"Percentage: {percentage}%")
    print(f"Second Number: {second_number}")

if __name__ == "__main__":
    calculate_second_number()
