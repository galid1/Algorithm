from datetime import datetime, timedelta

ymdh = str(datetime.utcnow() + timedelta(hours=9))
print(ymdh[:10])