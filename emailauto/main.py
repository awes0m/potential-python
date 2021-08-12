
import smtplib
emailadress = "somdevalmighty@gmail.com"
epassword = "Aware@1323"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=emailadress, password=epassword)
    connection.sendmail(from_addr=emailadress,
                        to_addrs="atoshidswt@gmail.com",
                        msg="Subject:Nose\n\nWarning!Give me NOSE immediately")
'''
import datetime as dt
now= dt.datetime.now()
year= now.year
day=now.weekday()
weekcheck=now.isoweekday()
print(now,year,day,weekcheck)
dob=dt.datetime(year=1995, month=0o3, day=10)
print(dob)
'''