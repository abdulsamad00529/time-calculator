# 🕒 Time Calculator

This is a Python project that defines a function `add_time()` to perform time arithmetic. It takes a start time, a duration to add, and optionally a starting day of the week, and returns the resulting time in a readable format.

## 📌 Features

- Accepts 12-hour clock time with AM/PM format.
- Handles duration additions involving hours and minutes.
- Accurately transitions between AM and PM, including midnight and noon.
- Supports optional day of the week and updates it accordingly.
- Returns information about how many days later the result occurs.
- Does **not** use any external libraries—just pure Python.


## 📥 Function Signature

```python
add_time(start, duration, starting_day=None)
```

### Parameters:

- `start` (str): Starting time in format `"HH:MM AM/PM"` (e.g. `"3:00 PM"`)
- `duration` (str): Duration to add in format `"H:MM"` (e.g. `"2:30"`)
- `starting_day` (str, optional): Day of the week (e.g. `"Monday"`, case insensitive)

### Returns:

- `str`: The updated time in the same format, including the correct AM/PM, day of the week if provided, and how many days later (if any).


## ✅ Example Usage

```python
print(add_time("3:00 PM", "3:10"))
# ➜ "6:10 PM"

print(add_time("11:30 AM", "2:32", "Monday"))
# ➜ "2:02 PM, Monday"

print(add_time("10:10 PM", "3:30"))
# ➜ "1:40 AM (next day)"

print(add_time("11:43 PM", "24:20", "tueSday"))
# ➜ "12:03 AM, Thursday (2 days later)"
```

## 📁 File Structure

```
📦 time_calculator_project/
├── time_calculator.py     # Contains the add_time() function
└── README.md              # Project documentation
```

## 🧠 Concepts Used

- String manipulation
- Conditional logic
- 24-hour and 12-hour time conversion
- Modular arithmetic
- Day of the week calculations
- Handling optional arguments in functions

## 🚀 Getting Started

No installation required. Just run the `add_time()` function in any Python 3 environment:

```
python3
>>> from time_calculator import add_time
>>> add_time("9:15 PM", "5:30")
```

## 🛠️ To-Do / Improvements

- Add a command-line interface (CLI)
- Create a simple GUI using Tkinter or PyQt
- Write unit tests for edge cases

## 🙋‍♂️ Connect with Me

- GitHub: [abdulsamad00529](https://github.com/abdulsamad00529)
- LinkedIn: [Abdul Samad](https://www.linkedin.com/in/abdul-samad-113aa5248/)

## 📄 License

This project is open-source and free to use for educational and learning purposes.

