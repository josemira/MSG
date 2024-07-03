Explanation:
1. `is_leap_year(year)`: Determines if a year is a leap year.
   - Time complexity: O(1)

2. `days_in_month(year, month)`: Determines the number of days in a given month of a given year.
   - Time complexity: O(1)

3. `days_from_start_of_year(year, month, day)`: Calculates the total number of days from the start of the year up to the given date.
   - Time complexity: O(1)

4. `days_since_reference_date(year, month, day)`: Calculates the total number of days from a fixed reference date (January 1, 0001) to the given date.
   - It first calculates the number of days in the full years since the reference date using:
     - days = (year - 1) * 365 + (year - 1) // 4 - (year - 1) // 100 + (year - 1) // 400
     - This accounts for leap years correctly.
   - Then, it adds the number of days in the current year up to the given date using `days_from_start_of_year`.
   - Time complexity: O(1)

5. `day_of_week(year, month, day)`: Uses Zeller's Congruence to find the day of the week for a given date.
   - Adjusts the month and year for January and February.
   - Uses a formula involving the day, month, and year to compute the day of the week.
   - Returns a value from 0 to 6 representing Monday to Sunday.
   - Time complexity: O(1)

6. `count_weekdays(start_year, start_month, start_day, end_year, end_month, end_day)`: 
   - Calculates the total number of days since the reference date for both the start and end dates using `days_since_reference_date`.
   - Calculates the total number of days between the two dates.
   - Determines the number of full weeks and the remaining days.
   - Uses the start day of the week to calculate the number of weekdays in the remaining days.
   - Full weeks contribute 5 weekdays each (Monday to Friday).
   - Remaining days are checked for weekdays (Monday to Friday).
   - Time complexity: O(1)

Overall Time Complexity:
- All the individual operations are O(1), making the overall time complexity of this program O(1).
