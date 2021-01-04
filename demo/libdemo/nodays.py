from datetime import datetime

try:
    s_sd = input("Enter start date [yyyymmdd] :")
    sd = datetime.strptime(s_sd, '%Y%m%d')

    s_ed = input("Enter end date [yyyymmdd]   :")
    ed = datetime.strptime(s_ed, '%Y%m%d')

    days = (ed - sd).days

    print(f"No. of days = {days}")
except:
    print("Error : Invalid Date. Please enter date in YYYYMMDD format")
