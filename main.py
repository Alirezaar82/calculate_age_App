#  -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import messagebox

import time
from datetime import datetime
from khayyam import JalaliDate
from calendar import isleap

def calculate_age(birthdate):
    current_date = datetime.now()
    age = current_date.year - birthdate.year
    if (current_date.month, current_date.day) < (birthdate.month, birthdate.day):
        age -= 1
    return age

def jalali_to_gregorian(jalali_date):
    gregorian_date = jalali_date.todate()
    return gregorian_date

def get_month(year):
    return year * 12 + localtime.tm_mon

def month_days(month, leap_year):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif month == 2 and leap_year:
        return 29
    elif month == 2 and not leap_year:
        return 28

def judge_leap_year(year):
    if isleap(year):
        return True
    else:
        return False

def get_day(month, leap_year):
    day = 0
    for m in range(1, localtime.tm_mon):
        day = day + month_days(m, leap_year)
    return day

def get_hour(days):
    return days * 24

def get_second(days):
    return days * 24 * 3600

def calculate_age_details():
    global localtime
    name = name_entry.get()
    try:
        year = int(year_entry.get())
        month = int(month_entry.get())
        day = int(day_entry.get())
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers for year, month, and day.")
        return

    eng_or_ir = calendar_var.get()

    if eng_or_ir == "english":
        birthdate = datetime(year, month, day)
        age = calculate_age(birthdate)
    elif eng_or_ir == "iran":
        try:
            birthdate = JalaliDate(year, month, day)
        except ValueError:
            messagebox.showerror("Invalid date", "Please enter a valid Jalali date.")
            return
        birthdate = jalali_to_gregorian(birthdate)
        birthdate = datetime(birthdate.year, birthdate.month, birthdate.day)
        age = calculate_age(birthdate)

    localtime = time.localtime(time.time())
    leap_year = judge_leap_year(localtime.tm_year)

    year = int(age)
    month = get_month(year)
    day = get_day(month, leap_year)
    hour = get_hour(day)
    second = get_second(day)

    begin_year = int(localtime.tm_year) - year
    end_year = begin_year + year

    for y in range(begin_year, end_year):
        if judge_leap_year(y):
            day = day + 366
        else:
            day = day + 365

    leap_year = judge_leap_year(localtime.tm_year)
    day = day + localtime.tm_mday

    # result_label.config(text=f"{name}'s age is {year} years or {month} months or {day} days or {hour} hours or {second} seconds")
    messagebox.showinfo("info", f"{name}'s age is {year} years or {month} months or {day} days or {hour} hours or {second} seconds")

# Create the main window
root = tk.Tk()
root.title("Age Calculator")

root.resizable(False, False)

tk.Label(root, text="Your Name:").grid(row=0, column=0, padx=10, pady=5)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Year of Birth:").grid(row=1, column=0, padx=10, pady=5)
year_entry = tk.Entry(root)
year_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Month of Birth:").grid(row=2, column=0, padx=10, pady=5)
month_entry = tk.Entry(root)
month_entry.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Day of Birth:").grid(row=3, column=0, padx=10, pady=5)
day_entry = tk.Entry(root)
day_entry.grid(row=3, column=1, padx=10, pady=5)

calendar_var = tk.StringVar(value="english")
tk.Label(root, text="Calendar System:").grid(row=4, column=0, padx=10, pady=5)
tk.Radiobutton(root, text="English", variable=calendar_var, value="english").grid(row=4, column=1, padx=10, pady=5)
tk.Radiobutton(root, text="Iranian", variable=calendar_var, value="iran").grid(row=5, column=1, padx=10, pady=5)

calculate_button = tk.Button(root, text="Calculate Age", command=calculate_age_details,bg='gray')
calculate_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

result_label = tk.Label(root, text="")
result_label.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
