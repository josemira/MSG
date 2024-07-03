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

def days_from_start_of_year(year, month, day):
    days = day
    for m in range(1, month):
        days += days_in_month(year, m)
    return days

def days_since_reference_date(year, month, day):
    # Number of days in full years since 0001
    days = (year - 1) * 365 + (year - 1) // 4 - (year - 1) // 100 + (year - 1) // 400
    
    # Number of days in the current year up to the given date
    days += days_from_start_of_year(year, month, day)
    
    return days

def day_of_week(year, month, day):
    if month < 3:
        month += 12
        year -= 1
    K = year % 100
    J = year // 100
    f = day + 13 * (month + 1) // 5 + K + K // 4 + J // 4 + 5 * J
    return (f + 5) % 7  # 0=Monday, 1=Tuesday, ..., 6=Sunday

def count_weekdays(start_year, start_month, start_day, end_year, end_month, end_day):
    start_days = days_since_reference_date(start_year, start_month, start_day)
    end_days = days_since_reference_date(end_year, end_month, end_day)
    
    total_days = end_days - start_days + 1  # Include end date

    # Calculate number of full weeks and remaining days
    full_weeks = total_days // 7
    remaining_days = total_days % 7

    weekdays = full_weeks * 5

    # Determine the start day of the week
    start_day_of_week = day_of_week(start_year, start_month, start_day)

    # Calculate weekdays in the remaining days
    for i in range(remaining_days):
        current_day_of_week = (start_day_of_week + i) % 7
        if current_day_of_week < 5:  # Monday to Friday
            weekdays += 1

    return weekdays

# Example usage:
start_year, start_month, start_day = 2023, 6, 26
end_year, end_month, end_day = 2023, 7, 2
print(count_weekdays(start_year, start_month, start_day, end_year, end_month, end_day))
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

def days_from_start_of_year(year, month, day):
    days = day
    for m in range(1, month):
        days += days_in_month(year, m)
    return days

def days_since_reference_date(year, month, day):
    # Number of days in full years since 0001
    days = (year - 1) * 365 + (year - 1) // 4 - (year - 1) // 100 + (year - 1) // 400
    
    # Number of days in the current year up to the given date
    days += days_from_start_of_year(year, month, day)
    
    return days

def day_of_week(year, month, day):
    if month < 3:
        month += 12
        year -= 1
    K = year % 100
    J = year // 100
    f = day + 13 * (month + 1) // 5 + K + K // 4 + J // 4 + 5 * J
    return (f + 5) % 7  # 0=Monday, 1=Tuesday, ..., 6=Sunday

def count_weekdays(start_year, start_month, start_day, end_year, end_month, end_day):
    start_days = days_since_reference_date(start_year, start_month, start_day)
    end_days = days_since_reference_date(end_year, end_month, end_day)
    
    total_days = end_days - start_days + 1  # Include end date

    # Calculate number of full weeks and remaining days
    full_weeks = total_days // 7
    remaining_days = total_days % 7

    weekdays = full_weeks * 5

    # Determine the start day of the week
    start_day_of_week = day_of_week(start_year, start_month, start_day)

    # Calculate weekdays in the remaining days
    for i in range(remaining_days):
        current_day_of_week = (start_day_of_week + i) % 7
        if current_day_of_week < 5:  # Monday to Friday
            weekdays += 1

    return weekdays

# Example usage:
start_year, start_month, start_day = 2023, 6, 26
end_year, end_month, end_day = 2023, 7, 2
print(count_weekdays(start_year, start_month, start_day, end_year, end_month, end_day))
