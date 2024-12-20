# Your Name: Angel Liriano
# Date: 10-6-2024
# Assignment Name: P2LAB2_LirianoAngel
# A brief description: This program stores a dictionary of vehicles and their MPG (miles per gallon). 
#                      It prompts the user to enter a vehicle, then calculates and displays the number of gallons needed 
#                      for a given number of miles to drive that vehicle.

# Dictionary with vehicle models and their respective MPG values
vehicles_mpg = {
    "Camaro": 18.21,
    "Prius": 52.36,
    "Model S": 110,
    "Silverado": 26
}

# Get the keys from the dictionary
vehicle_keys = vehicles_mpg.keys()

# Print the available vehicle models (keys)
print("Available vehicles:")
for vehicle in vehicle_keys:
    print(vehicle)

# Prompt the user to enter a vehicle name
selected_vehicle = input("\nEnter the name of a vehicle from the list above: ")

# Ensure the entered vehicle is in the dictionary
if selected_vehicle in vehicles_mpg:
    # Get the MPG for the selected vehicle
    mpg = vehicles_mpg[selected_vehicle]
    print(f"The {selected_vehicle} has an MPG of {mpg}.")

    # Prompt the user to enter the number of miles they plan to drive
    miles_to_drive = float(input("Enter the number of miles you will drive: "))

    # Calculate the gallons of gas needed
    gallons_needed = miles_to_drive / mpg

    # Display the calculated gallons, rounded to 2 decimal places
    print(f"To drive {miles_to_drive} miles in a {selected_vehicle}, you will need {gallons_needed:.2f} gallons of gas.")
else:
    print("The vehicle you entered is not available in the list. Please try again.")
