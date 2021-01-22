def add_time(start, duration, day=''):
    start, duration = start.split(), duration
    additional_hours = 0
    days = 0
    time = start[1]
    new_time = ''
    onset = start[0].split(':')
    offset = duration.split(':')
    minutes = int(onset[1]) + int(offset[1])
    if minutes >= 60:
        additional_hours = 1
        minutes -= 60
    if len(str(minutes)) == 1:
        minutes = '0' + str(minutes)
    else:
        minutes = str(minutes)
    hours = int(onset[0]) + int(offset[0]) + additional_hours
    if hours >= 12:
        cycles = hours // 12
        days = hours // 24
        if cycles > 0 and time == 'PM':
            days += 1
        if (cycles % 2) != 0:
            if time == 'PM':
                time = 'AM'
            else:
                time = 'PM'
        hours = hours - (12 * cycles)
        if hours == 0:
            hours = 12
    hours = str(hours)
    if not day:
        if days == 0:
            new_time = hours + ':' + minutes + ' ' + time
        elif days == 1:
            new_time = hours + ':' + minutes + ' ' + time + ' (next day)'
        else:
            new_time = hours + ':' + minutes + ' ' + time + ' ({} days later)'.format(days)
    else:
        day = day.lower()
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
    return new_time