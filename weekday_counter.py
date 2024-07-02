from datetime import datetime, timedelta

def count_weekdays(start_date, end_date):
    # Convert strings to datetime objects
    start_date = datetime.strptime(start_date, "%Y-%m-%d")
    end_date = datetime.strptime(end_date, "%Y-%m-%d")
    
    # Ensure start_date is before end_date
    if start_date > end_date:
        start_date, end_date = end_date, start_date

    total_days = (end_date - start_date).days + 1  # inclusive of both start and end dates
    
    full_weeks = total_days // 7
    remaining_days = total_days % 7
    
    # Count the number of weekdays in the remaining days
    weekdays = 0
    for i in range(remaining_days):
        if (start_date + timedelta(days=i)).weekday() < 5:
            weekdays += 1
    
    return full_weeks * 5 + weekdays

# Example usage
start_date = "2023-06-01"
end_date = "2023-06-14"
print(count_weekdays(start_date, end_date))  # Output: 10
