
def add_time(start_time, duration, week_day=''):
    s_time, clock_format = start_time.split(' ')

    start_hh_mm = [int(a) for a in s_time.split(':')]
    duration_hh_mm = [int(b) for b in duration.split(':')]

    if clock_format == 'PM':
        start_hh_mm[0] = start_hh_mm[0] + 12

    result = [start_hh_mm[0] + duration_hh_mm[0],
              start_hh_mm[1] + duration_hh_mm[1]]

    result[0] = int(result[0] + (result[1] - result[1] % 60) / 60)
    result[1] = str(int(result[1] % 60))

    if len(result[1]) == 1:
        result[1] = '0' + result[1]

    # find n days
    rest_hh_on_d = result[0] % 24
    n_days = (result[0] - rest_hh_on_d) / 24

    result[0] = rest_hh_on_d
    if (result[0] / 12) > 1:
        result[0] = result[0] - 12
        result_clock_format = 'PM'
    elif (result[0] / 12) == 1:
        result_clock_format = 'PM'
    else:
        result_clock_format = 'AM'

    if result[0] == 0:
        result[0] = 12

    result[0] = str(int(result[0]))
    # result string
    result_string = ':'.join(result) + ' ' + result_clock_format

    # find the day
    if len(week_day) != 0:
        days = ['Monday',
                'Tuesday', 'Wednesday',
                'Thursday', 'Friday', 'Saturday',
                'Sunday']

        rest_days = n_days % 7
        first_day_of_week = 0

        for x, value in enumerate(days):
            if value == week_day:
                first_day_of_week = x

        index_of_result = first_day_of_week + rest_days

        if index_of_result <= len(week_day) - 1:
            result_day = days[int(index_of_result)]
        else:
            result_day = days[len(week_day) - int(index_of_result)]

        result_string = result_string + ', ' + result_day
        if n_days > 1:
            result_string = result_string + ' ' + '({} days later)'.format(str(int(n_days)))
        elif n_days == 1:
            result_string = result_string + ' ' + '(next day)'
        else:
            pass
    else:
        if n_days > 1:
            result_string = result_string + ' ' + '({} days later)'.format(str(int(n_days)))
        elif n_days == 1:
            result_string = result_string + ' ' + '(next day)'
        else:
            pass

    return result_string


if __name__ == '__main__':
    print(add_time("6:30 PM", "205:12"))
