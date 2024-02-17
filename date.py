from datetime import datetime

# Get the current date and time
current_date_time = datetime.now()

# Format the date and time as a string
formatted_date_time = current_date_time.strftime("%Y-%m-%d %H:%M:%S")

# Display the result
print("Current Date and Time:", formatted_date_time)
