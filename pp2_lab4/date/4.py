from datetime import datetime
date1=datetime(2025,1,10,14,30,0)
date2=datetime(2025,1,15,10,15,30)
diff=abs(date2-date1)
seconds=diff.total_seconds()
print(seconds)
