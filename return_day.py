#my solution, a quite obvious one   

def return_day(number):
    days = ["Sunday", 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    if number == 1:
        return days[0]
    elif number == 2:
        return days[1]
    elif number == 3:
        return days[2]
    elif number == 4:
        return days[3]
    elif number == 5:
        return days[4]
    elif number == 6:
        return days[5]
    elif number == 7:
        return days[6]
    else:
        return None
        
#course answer

def return_day(num):
    days = ["Sunday","Monday", "Tuesday","Wednesday","Thursday","Friday","Saturday"]
    # Check to see if num valid
    if num > 0 and num <= len(days):
        # use num - 1 because lists start at 0 
        return days[num-1]
    return None
