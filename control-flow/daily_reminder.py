# daily_reminder.py


    # Prompt for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

    # Validate priority input
if priority not in ["high", "medium", "low"]:
    print("Invalid priority level. Please enter 'high', 'medium', or 'low'.")

    # Generate reminder based on priority and time sensitivity
match priority:
    case "high":
            reminder = f"'{task}' is a high priority task."
    case "medium":
            reminder = f"'{task}' is a medium priority task."
    case "low":
            reminder = f"'{task}' is a low priority task."

    # Modify reminder if task is time-bound
if time_bound == "yes":
    reminder += " that requires immediate attention today!"
else:
    reminder += " Consider completing it when you have free time."

    # Print the customized reminder
print("Reminder:", reminder)