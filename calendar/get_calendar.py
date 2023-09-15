from icalevents.icalevents import events

events = events("https://calendar.google.com/calendar/ical/jo-bell%40live.co.uk/"
                "private-1663142b1daf9a471001bf725ef93324/basic.ics")

for individual_event in events:
    print(individual_event.summary, individual_event.start, individual_event.end)
