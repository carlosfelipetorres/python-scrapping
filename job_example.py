from crontab import CronTab

cron = CronTab(user='lealcolombia2')
# /usr/bin/python3 /Users/lealcolombia2/Desktop/integras/example1.py
job = cron.new(command='cd Desktop/integras && /usr/bin/python3 /Users/lealcolombia2/Desktop/integras/example1.py >> test.out')
job.minute.every(1)
cron.write()