# daily_reminder.py


    # Prompt for a single task
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

if time_bound == "yes" and priority in {"high", "medium", "low"}:
    reminder = f"Reminder: '{task}' is a {priority} priority task that requires immediate attention today!"
else:
    reminder = f"Reminder: '{task}' is a {priority} priority task."

    # Process the task based on priority and time sensitivity
match priority:
    case "high":
            reminder += " This task is critical and should be addressed immediately."
    case "medium":
            reminder += " This task is important but can be scheduled for later today."
    case "low":
            reminder += " This task is not urgent and can be done at your convenience."
    case _:
            reminder = "Invalid priority entered. Please use 'high', 'medium', or 'low'."
    
    # Provide the customized reminder
print(reminder)