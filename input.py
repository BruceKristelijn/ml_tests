from datetime import datetime

# Requests the timeframe from the user.
def getTimeFrameInput():
    # Define variables
    timeframe_in_seconds = 0

    # Request the timeframe and parse. If this is not possible return.
    while(True):
        # Get the timeframe
        frame = str(input("Please select timeframe (ex. 4H, 10M, 60):"))

        # Check if numeric
        if frame.isnumeric():
            # If is numeric parse to seconds
            timeframe_in_seconds = int(frame)
            break # Exit input loop

        # Check if last is input
        lastString = frame[-1].upper()
        number = frame[0:-1]

        # Check numeric
        if number.isnumeric()is False:
            print("Given string is not a number or timeframe. Please lookout for any characters")
            continue
        else:
            number = int(number)

        if lastString in ['S', 'M', 'H', 'D', 'W']: # Seconds, Month, Hour, Day, Week
            if lastString == 'S':
                timeframe_in_seconds = number
            
            if lastString == 'M':
                timeframe_in_seconds = number * 60

            if lastString == 'H':
                timeframe_in_seconds = number * 60 * 60

            if lastString == 'D':
                timeframe_in_seconds = number * 60 * 60 * 24

            if lastString == 'W':
                timeframe_in_seconds = number * 60 * 60 * 24 * 7

            break

        print("Cannot read input. Please try again. \n")

    return(timeframe_in_seconds)

# Requests a date as input from user.
def getDateInput():
    # Define variables
    timeframe_in_seconds = 0

    # Request the date and parse or try again.
    while(True):
        date = input("Please input a date (%d/%m/%y ex. 12-12-20 = 12 Dec 2020):")

        if date.upper() == 'TODAY':
            return datetime.today()

        try:
            datetime_object = datetime.strptime(date,"%d/%m/%y")
            return datetime_object
        except ValueError as err:
            print(err)
            print("Datetime is not correct: \n Please try again.")

def getTickerInput():
    ticker = input("Selected ticker:")
    return ticker