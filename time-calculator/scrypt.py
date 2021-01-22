start, duration = "9:15 PM".split(), "5:30"

onset = start[0].split(':')

offset = duration.split(':')

additional_hours = 0

time = start[1]

days = 0

minutes = int(onset[1]) + int(offset[1])

if minutes >= 60:
    additional_hours = 1
    minutes -= 60

if len(str(minutes)) == 1:
    minutes = '0' + str(minutes)
else:
    minutes = str(minutes)

hours = int(onset[0]) + int(offset[0]) + additional_hours

days = hours // 24

cycles = hours // 12

if (cycles % 2) != 0:
    if time == 'PM':
        time = 'AM'
    else:
        time = 'PM'

if time == 'PM' and (cycles > 0):
    days += + 1

if hours > 12:
    hours = hours - (12 * cycles)
    if hours == 0:
        hours = 12

hours = str(hours)

day = "Monday".lower()

week = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

weekday = week.index(day)

weekday = weekday + days - (7 * (days//7))

if weekday > 6:
    weekday = weekday - 7

final_day = week[weekday]

if days == 0:
    new_time = hours + ':' + minutes + ' ' + time + ', ' + final_day.title()
elif days == 1:
    new_time = hours + ':' + minutes + ' ' + time + ', ' + final_day.title() + ' (next day)'
else:
    new_time = hours + ':' + minutes + ' ' + time + ', ' + final_day.title() + ' ({} days later)'.format(days)

print(new_time)