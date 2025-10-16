from datetime import date

def days_until_new_year():
    today = date.today()
    next_year = today.year + 1
    new_year = date(next_year, 1, 1)
    
    days_left = (new_year - today).days
    
    print(f"Today is: {today}")
    print(f"Days until New Year ({next_year}): {days_left} days")

if __name__ == "__main__":
    days_until_new_year()