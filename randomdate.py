from random import randrange
from datetime import datetime, timedelta

def random_date(start, end):
    """
    This function will return a random datetime between two datetime 
    objects.
    """
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)

def randome_range():
    # Specify range
    d1 = datetime.strptime('3/1/2022 01:00 PM', '%m/%d/%Y %I:%M %p')
    d2 = datetime.strptime('11/30/2022 01:00 PM', '%m/%d/%Y %I:%M %p')

    # Make sure date is no weekend
    while(True):
        date = random_date(d1, d2)
        dayNumber = datetime.today().weekday()

        if dayNumber < 5:
            break
        else:  # 5 Sat, 6 Sun
            continue

    return date
