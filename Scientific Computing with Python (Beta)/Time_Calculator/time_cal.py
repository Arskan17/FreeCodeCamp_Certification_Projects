def add_time(start, duration):
    AM = 1
    if start[-2] == 'A':
        AM = 0

    start_hour = 0
    start_minutes = 0
    if len(start) == 8:
        start_hour = int(start[0] + start[1])
        start_minutes = int(start[3] + start[4])
    elif len(start) == 7:
        start_hour = int(start[0])
        start_minutes = int(start[2] + start[3])
        
    # print(start_hour, start_minutes) # print to make sure

    duration_hour = 0
    duration_minutes = 0
    if len(duration) == 5:
        duration_hour = int(duration[0] + duration[1])
        duration_minutes = int(duration[3] + duration[4])
    elif len(duration) == 4:
        duration_hour = int(duration[0])
        duration_minutes = int(duration[2] + duration[3])
        
    # print(duration_hour, duration_minutes) # print to make sure

    
    end_hour = (start_hour + duration_hour + ((start_minutes + duration_minutes) // 60))%12
    # print(end_hour)
    end_minutes = (start_minutes + duration_minutes)%60    
    # print(end_minutes)

    AM = (AM + (start_hour + duration_hour + ((start_minutes + duration_minutes) // 60))//12)%2

    sufx = ''
    if AM==0:
        sufx = 'AM'
    elif AM==1:
        sufx = 'PM'
    
    if end_minutes < 10:
        return str(end_hour) + ':0' + str(end_minutes) + ' ' + sufx
    

    return str(end_hour) + ':' + str(end_minutes) + ' ' + sufx






''' test examples to run code '''

# print(add_time('3:30 PM', '2:12'))
# print(add_time('11:55 AM', '3:12'))
print(add_time('8:16 PM', '69:02'))
