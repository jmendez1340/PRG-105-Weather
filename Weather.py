# Average Temperature monthly in Seville
# http://www.holiday-weather.com/seville/averages/

Average_Temperature = {'Jan': 52, 'Feb': 54, 'Mar': 59,'Apr': 64,'May': 68,'June': 77,'July': 82,'Aug': 82, 'Sept': 77, 'Oct': 68, 'Nov': 59, 'Dec': 54}

# Global variables
average = 66

warmest = dict()

def Monthly(day):
    total = 0
    for ly in day:
        total += day[ly]
    print("The average temperature in Seville is " + str(average) + " degrees fahrenheit.\n")
    # Line break to make reading easier


def Temp(today):
    global average
    for ly in today:
        if today[ly] > average:
            warmest[ly] = (today[ly])
    print (" The Warmest months in Seville are \n " + str(warmest))
    # Chose to make the break after are because it just seems easier to read that way

Monthly(Average_Temperature)
Temp(Average_Temperature)