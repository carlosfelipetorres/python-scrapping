from crontab import CronTab

cron = CronTab(user=True)
job = cron.new(command='/usr/bin/python3 integras_login.py')
# job.every(2).minutes()

job.enable(False)

print(job)
print(cron)

cron.write()