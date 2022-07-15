def add_time(start: str, duration: str, given_day: str =''):
    """Add the duration time to the start time and return the result.

    Args:
        start (str): Start time in the 12-hour clock format (ending in AM or PM)
        duration (str): A duration time that indicates the number of hours and minutes
        given_day (str, optional): A starting day of the week, case insensitive. 
                                 - Defaults to ''.

    Returns:
        str: New Time in 12-hour clock format ending in AM or PM
    """
    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    
    starting_day: str = given_day.capitalize()
    if starting_day not in days:
        starting_day = 'Monday'
    
    time_states = ['AM','PM']
    
    # Separating starting hour from 'minute with time state'
    start_time: list[str] = start.split(':')
    start_hour: str = start_time[0]
    minute_with_time_state: str = start_time[1].lower()
    
    # Separating start minute and time state
    am: bool = 'a' in minute_with_time_state
    pm: bool = 'p' in minute_with_time_state
    
    if am == 1:
        index: int = minute_with_time_state.find(('a'))
        start_minute: str = minute_with_time_state[0:index].strip() 
        time_state: str = minute_with_time_state[index:].upper().strip()
        
    elif pm ==1:
        index: int = minute_with_time_state.find(('p'))
        start_minute: str = minute_with_time_state[0:index].strip() 
        time_state: str = minute_with_time_state[index:].upper().strip()
    else:
        return 'Ensure time ending in AM or PM'
        quit()
    
    if time_state not in time_states:
        return 'Ensure time ending in AM or PM'
        quit()
       
    # Documenting Duration
    added_time: list[str] = duration.split(':')
    added_hour: str = added_time[0]
    added_minute: str = added_time[1]
    
    sum_of_minutes: int = int(start_minute)+int(added_minute)
    
    #Computing Minutes
    minute_hour: int = 0
    new_minute: int = sum_of_minutes
    
    while new_minute >= 60:
        new_minute -= 60
        minute_hour += 1
    
    #Computing hours
    new_days:int = 0
    sum_of_hours: int = int(start_hour) + int(added_hour) + int(minute_hour)
    
    new_hour: int = sum_of_hours
    while new_hour > 24: 
        new_hour -= 24
        new_days += 1
    
    # Determining AM/PM
    new_time_state: str = time_state
    while new_hour > 12:
        new_hour -= 12
        if time_state == 'AM':
            new_time_state = 'PM'
        else:
            new_time_state = 'AM'
            new_days += 1
    
    if new_hour == 12:
        if time_state == 'AM':
            new_time_state = 'PM'
        else:
            new_time_state = 'AM'
            new_days += 1
            
    # Defining new day        
    if new_days > 0:
        index: int = days.index(starting_day)
        new_index: int = index + new_days
        
        while new_index >= len(days) - 1:
            new_index -= len(days)
            
        new_day: str = days[new_index]
    
    else:
        new_day = starting_day
        
    # Defining next day printing format
    if new_days > 1:
        next_day = f' ({new_days} days later)'
    elif new_days == 1:
        next_day = f' (next day)'
    else:
        next_day = ''



    if given_day != '':
        new_time: str = f'{new_hour}:{new_minute:0>2} {new_time_state}, {new_day}{next_day}'
    else:
        new_time: str = f'{new_hour}:{new_minute:0>2} {new_time_state}{next_day}'
    
    return new_time

if __name__ == '__main__':
    print(add_time("11:40 Am", "12:25"))
