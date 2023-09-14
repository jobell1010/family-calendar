from icalevents.icalevents import events

es = events("https://calendar.google.com/calendar/ical/jo-bell%40live.co.uk/"
            "private-1663142b1daf9a471001bf725ef93324/basic.ics")

for i in es:
    print(i)
    