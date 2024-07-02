def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_month(year, month):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif month == 2:
        return 29 if is_leap_year(year) else 28
    return 0

def days_between_dates(start_year, start_month, start_day, end_year, end_month, end_day):
    total_days = 0
    # Count days from start date to the end of the start month
    total_days += days_in_month(start_year, start_month) - start_day + 1
    
    # Count days for the full months between the start and end dates
    current_year, current_month = start_year, start_month + 1
    while (current_year < end_year) or (current_year == end_year and current_month < end_month):
        total_days += days_in_month(current_year, current_month)
        current_month += 1
        if current_month > 12:
            current_month = 1
            current_year += 1

    # Count days from the beginning of the end month to the end date
    total_days += end_day

    return total_days

def day_of_week(year, month, day):
    if month < 3:
        month += 12
        year -= 1
    K = year % 100
    J = year // 100
    f = day + 13*(month+1)//5 + K + K//4 + J//4 + 5*J
    return f % 7  # 0=Saturday, 1=Sunday, 2=Monday, ..., 6=Friday

def count_weekdays(start_year, start_month, start_day, end_year, end_month, end_day):
    total_days = days_between_dates(start_year, start_month, start_day, end_year, end_month, end_day)
    start_day_of_week = day_of_week(start_year, start_month, start_day)
    
    weekdays = 0
    for i in range(total_days):
        current_day_of_week = (start_day_of_week + i) % 7
        if current_day_of_week not in [0, 1]:  # Exclude Saturday (0) and Sunday (1)
            weekdays += 1

    return weekdays

# Example usage:
start_year, start_month, start_day = 2023, 6, 26
end_year, end_month, end_day = 2023, 7, 2
print(count_weekdays(start_year, start_month, start_day, end_year, end_month, end_day))
