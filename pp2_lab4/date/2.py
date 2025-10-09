from datetime import datetime,timedelta
current_date=datetime.now()
yesterday=current_date-timedelta(days=1)
tomorrow=current_date+timedelta(days=1)
print(yesterday.strftime('%A,%B %d,%Y'))
print(current_date.strftime('%A,%B %d,%Y'))
print(tomorrow.strftime('%A,%B %d,%Y'))