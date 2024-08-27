import os

f = open('login-app-chart/Chart.yaml','r')
lines = f.readlines()
for row in lines:
    if row.startswith("name"):
        chart=row
    if row.startswith("version"):
        version=row


chart_name=chart.split(" ")
ver=version.split(" ")
print(chart_name[1].strip())
f.close()


