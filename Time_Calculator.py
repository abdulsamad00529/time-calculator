def add_time(start, duration, starting_day=None):
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    # Parse start time
    time_part, meridiem = start.split()
    start_hour, start_minute = map(int, time_part.split(':'))

    # Convert to 24-hour time
    if meridiem == "PM" and start_hour != 12:
        start_hour += 12
    elif meridiem == "AM" and start_hour == 12:
        start_hour = 0

    # Parse duration
    duration_hour, duration_minute = map(int, duration.split(':'))

    # Add time
    total_minutes = start_minute + duration_minute
    extra_hour = total_minutes // 60
    end_minute = total_minutes % 60

    total_hours = start_hour + duration_hour + extra_hour
    days_later = total_hours // 24
    end_hour_24 = total_hours % 24

    # Convert back to 12-hour time
    if end_hour_24 == 0:
        display_hour = 12
        display_meridiem = "AM"
    elif end_hour_24 < 12:
        display_hour = end_hour_24
        display_meridiem = "AM"
    elif end_hour_24 == 12:
        display_hour = 12
        display_meridiem = "PM"
    else:
        display_hour = end_hour_24 - 12
        display_meridiem = "PM"

    # Format minutes
    display_minute = f"{end_minute:02}"

    # Build final time string
    new_time = f"{display_hour}:{display_minute} {display_meridiem}"

    # Add day of the week if provided
    if starting_day:
        start_index = days_of_week.index(starting_day.capitalize())
        new_day = days_of_week[(start_index + days_later) % 7]
        new_time += f", {new_day}"

    # Add day count info
    if days_later == 1:
        new_time += " (next day)"
    elif days_later > 1:
        new_time += f" ({days_later} days later)"

    return new_time



print(add_time('3:00 PM', '3:10'))  # ➜ 6:10 PM
print(add_time('11:30 AM', '2:32', 'Monday'))  # ➜ 2:02 PM, Monday
print(add_time('11:43 AM', '00:20'))  # ➜ 12:03 PM
print(add_time('10:10 PM', '3:30'))  # ➜ 1:40 AM (next day)
print(add_time('11:43 PM', '24:20', 'tueSday'))  # ➜ 12:03 AM, Thursday (2 days later)
print(add_time('6:30 PM', '205:12'))  # ➜ 7:42 AM (9 days later)
