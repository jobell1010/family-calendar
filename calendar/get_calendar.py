from icalevents.icalevents import events
from flask import Flask

app = Flask(__name__)


def get_events():
    items = []
    ev_list = events(file="basic.ics", sort=True)
    for individual_event in ev_list:
        # print(individual_event.summary)
        # print(individual_event.start)
        # print(individual_event.end)
        event_title = individual_event.summary
        items.append(event_title)
    return items


# event_names = get_events()
# print(event_names)

@app.route('/')
def calendar():
    event = get_events()
    return event
