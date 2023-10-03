from get_calendar import get_events
from flask_table import Table, Col
from flask import Flask, render_template

event_list = get_events()


class EventTable(Table):
    event = Col('Event')
    start = Col('Start')
    end = Col('End')


class Event(object):
    def __init__(self, event, start, end):
        self.event = event
        self.start = start
        self.end = end


items = [Event(a, b, c) for a, b, c in event_list]

table_html = EventTable(items)
# print(table.__html__())

app = Flask(__name__)


@app.route('/')
def table():
    return render_template('table.html', table=table_html)
