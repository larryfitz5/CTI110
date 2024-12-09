# Angel Liriano
# Date: 11-10-24
# Assignment: P4HW1_LirianoAngel83
# This program collects a user-defined number of scores, validates each score,
# calculates the average after dropping the lowest score, and displays the letter grade.

# Pseudocode:
# 1. Ask user for the number of scores they want to enter.
# 2. Initialize an empty list to store valid scores.
# 3. For each score:
#    - Prompt the user to enter a score.
#    - If score is valid (between 0 and 100), add to the list.
#    - If not valid, prompt the user to re-enter until valid.
# 4. Once all scores are entered:
#    - Display the lowest score.
#    - Remove the lowest score from the list and display the modified list.
#    - Calculate the average of the modified list and display it.
#    - Determine the letter grade based on the average and display it.

# Step 1: Ask for number of scores
num_scores = int(input("Enter the number of scores you would like to enter: "))

# Step 2: Initialize empty list to store scores
scores = []

# Step 3: Loop to collect and validate scores
for i in range(num_scores):
    while True:
        try:
            score = float(input(f"Enter score #{i + 1}: "))
            # Validate score
            if 0 <= score <= 100:
                scores.append(score)
                break  # Valid score, exit the while loop
            else:
                print("Invalid score. Please enter a score between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a numerical score.")

# Step 4: Process and display results
# Display the lowest score
lowest_score = min(scores)
print(f"\nLowest score: {lowest_score}")

# Remove the lowest score and display the modified list
scores.remove(lowest_score)
print(f"Modified list after dropping the lowest score: {scores}")

# Calculate and display the average
average_score = sum(scores) / len(scores)
print(f"Average score: {average_score:.2f}")

# Determine the letter grade
if average_score >= 90:
    letter_grade = "A"
elif average_score >= 80:
    letter_grade = "B"
elif average_score >= 70:
    letter_grade = "C"
elif average_score >= 60:
    letter_grade = "D"
else:
    letter_grade = "F"

print(f"Letter grade: {letter_grade}")
