import tkinter as tk
from datetime import datetime

def find_zodiac_sign(day, month):
    if (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return "Aries"
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return "Taurus"
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        return "Gemini"
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        return "Cancer"
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        return "Leo"
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        return "Virgo"
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        return "Libra"
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        return "Scorpio"
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        return "Sagittarius"
    elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
        return "Capricorn"
    elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return "Aquarius"
    elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
        return "Pisces"

def calculate_age(birth_date):
    today = datetime.now()
    age = today.year - birth_date.year
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1
    return age

def find_day_of_week(birth_date):
    return birth_date.strftime("%A")

def display_info():
    dob_str = entry_dob.get()
    try:
        birth_date = datetime.strptime(dob_str, "%d/%m/%Y")
        day = birth_date.day
        month = birth_date.month
        zodiac_sign = find_zodiac_sign(day, month)
        age = calculate_age(birth_date)
        day_of_week = find_day_of_week(birth_date)
        
        result.set(f"Zodiac Sign: {zodiac_sign}\nDay of Week: {day_of_week}\nAge: {age}")
    except ValueError:
        result.set("Invalid Date Format! Please enter as DD/MM/YYYY.")

# Tkinter GUI setup
root = tk.Tk()
root.title("Zodiac Sign Finder")

tk.Label(root, text="Enter your Date of Birth (DD/MM/YYYY):").pack(pady=10)
entry_dob = tk.Entry(root)
entry_dob.pack(pady=5)

tk.Button(root, text="Find", command=display_info).pack(pady=10)

result = tk.StringVar()
tk.Label(root, textvariable=result, font=("Arial", 12)).pack(pady=20)

root.mainloop()
