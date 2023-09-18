from icalevents.icalevents import events

ev_list = events(file="basic.ics", sort=True)

for individual_event in ev_list:
    start = individual_event.start

    print(individual_event.summary)
    print(individual_event.start)
    print(individual_event.end)
    print()
    