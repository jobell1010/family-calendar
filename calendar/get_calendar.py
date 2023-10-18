from icalevents.icalevents import events
from flask import Flask, render_template

app = Flask(__name__)


def get_events():
    items = []
    ev_list = events(file="basic.ics", sort=True)
    for individual_event in ev_list:
        event_title = individual_event.summary
        start = individual_event.start
        st_time = start.strftime("%A %d %B, %H:%M")
        end = individual_event.end
        end_time = end.strftime("%A %d %B, %H:%M")
        items.append([event_title, st_time, end_time])
    return items


@app.route('/')
def calendar():
    event_list = get_events()
    return render_template('calendar.html', event_list=event_list)


@app.route('/week')
def week():
    return render_template('week_to_view.html')
