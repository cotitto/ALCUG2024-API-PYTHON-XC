from canvasapi import Canvas
import csv
from datetime import datetime
import os
import pytz

# Initialize a new Canvas object
# url = os.environ['API_PROD_INSTANCE']
# token = os.environ['API_TOKEN']
# canvas = Canvas(url, token)

# Canvas API URL
API_URL = "REPLACEME"
# Canvas API key
API_KEY = "REPLACEME"
# Initialize a new Canvas object
canvas = Canvas(API_URL, API_KEY)

# Canvas Course ID
course = canvas.get_course(69319)
# Calendar Context Course ID
course_context_code = f"course_{course.id}"

# Get calendar events for the course
calendar_events = canvas.get_calendar_events(
    context_codes=[course_context_code],
    all_events="TRUE",
)

def gt_output_filename():

    now = datetime.now()
    yr= now.strftime("%Y")
    mo= now.strftime("%m")
    day=now.strftime("%d")
    #fname = 'Calendar_Events_3-' +str(yr)+'_'+str(mo)+'_'+str(day)+'.csv'
    fname = 'Calendar_Events_'f"{course.course_code} " + str(yr) + '_' + str(mo) + '_' + str(day) + '.csv'

    return fname

filename = gt_output_filename()
print(filename)

with open(filename,'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile,dialect='excel')
    writer.writerow(["event_id", "event_title", "event.start_at", "event.end_at", "event.description", "location_name", "event.context_code"])
    for event in calendar_events:
        # Define UTC timezone
        utc_timezone = pytz.utc
        # Define Central timezone
        central_timezone = pytz.timezone('America/Chicago')  # 'America/Chicago' corresponds to Central Time
        start_at_utc = datetime.strptime(event.start_at, "%Y-%m-%dT%H:%M:%S%z").replace(tzinfo=utc_timezone).astimezone(central_timezone)
        end_at_utc = datetime.strptime(event.end_at, "%Y-%m-%dT%H:%M:%S%z").replace(tzinfo=utc_timezone).astimezone(central_timezone)
        print(f"Event: {event.title}", f"location: {event.location_name}")
        print('-' * 75)
        csvdata = (event.id, event.title, start_at_utc, end_at_utc, event.description, event.location_name, event.context_code)

        writer.writerow(csvdata)

    print(f"Finished processing events for:{course.name}")
    print('-' * 75)
# Iterate through the calendar events and print details




