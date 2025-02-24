# unlimited percentage calculator
import numpy as np


def calculate_percentage():
    print("Enter the total value:")
    total = float(input())
    
    print("Enter the value to calculate percentage:")
    value = float(input())
    
    percentage = (value / total) * 100
    
    print(f"\nResults:")
    print(f"Value: {value}")
    print(f"Total: {total}")
    print(f"Percentage: {percentage:.2f}%")

if __name__ == "__main__":
    print("Percentage Calculator")
    print("-------------------")
    calculate_percentage()
