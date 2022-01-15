import datetime

time_now = datetime.datetime.now().isoformat()

with open(r'/mylogs/pythonscripts.log','a') as f:
    f.write(f'[{time_now}] Cron ran on python script "01-echo.py".')

    