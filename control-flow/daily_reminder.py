# daily_reminder.py


    # Prompt for a single task
task = input("Enter your task: ")
priority = input("priority (high, medium, low): ").lower()
time_bound = input("Is it time-bound? (yes or no): ").lower()

    # Process the task based on priority and time sensitivity
reminder = f"Reminder: '{task}' is a {priority} priority task."
    
match priority:
    case "high":
            reminder += " This task is critical and should be addressed immediately."
    case "medium":
            reminder += " This task is important but can be scheduled for later today."
    case "low":
            reminder += " This task is not urgent and can be done at your convenience."
    case _:
            reminder = "Invalid priority entered. Please use 'high', 'medium', or 'low'."
    
if time_bound == "yes" and priority in {"high", "medium", "low"}:
        reminder += " Additionally, this is a time-sensitive task that requires immediate attention today!"

    # Provide the customized reminder
print(reminder)