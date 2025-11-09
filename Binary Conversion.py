print("Welcome to the Number System Converter Project!")

# --- Outer Loop (using while True for continuous input) ---
while True:
    try:
        # Get input from the user
        decimal_num = int(input("\nEnter a positive decimal number (or enter 0 to exit): "))
        
        if decimal_num == 0:
            print("Exiting the program. Goodbye!")
            break # Exit the outer loop

        if decimal_num < 0:
            print("Please enter a positive number.")
            continue

        # List to store the binary remainders
        remainders = []
        original_num = decimal_num # Store original for printing later

        # --- Inner Loop (while loop for the conversion logic) ---
        while decimal_num > 0:
            remainder = decimal_num % 2 # Get the remainder (0 or 1)
            remainders.append(remainder) # Add it to our list
            decimal_num = decimal_num // 2 # Update the number by integer division
            
        # The remainders are in reverse order, so we need to reverse the list
        remainders.reverse()

        # --- Another Loop (for loop to print the result) ---
        # Convert the list of integers into a single binary string
        binary_result = ""
        for digit in remainders:
            binary_result = binary_result + str(digit)
            
        print(f"\nThe decimal number {original_num} is {binary_result} in binary.")
        
    except ValueError:
        print("Invalid input. Please enter a whole number.")


