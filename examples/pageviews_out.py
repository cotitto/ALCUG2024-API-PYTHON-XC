from canvasapi import Canvas
import os
import csv
from datetime import datetime
import pytz
from dateutil import tz


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

# Define UTC timezone
utc_timezone = pytz.utc

# Define Central timezone
central_timezone = pytz.timezone('America/Chicago')  # 'America/Chicago' corresponds to Central Time

# Define UTC datetime
utc_datetime = datetime.utcnow()

# Define the user ID for which you want to retrieve page views
user_id = "86226"

# Get the user object
user = canvas.get_user(user_id)

def gt_output_filename():

    now = datetime.now()
    yr = now.strftime("%Y")
    mo = now.strftime("%m")
    day = now.strftime("%d")
    fname = 'Pageviews_for_'+user.name+'_'+str(yr)+'_'+str(mo)+'_'+str(day)+'.csv'

    return fname

filename = gt_output_filename()
print(filename)

# Define the user ID for which you want to retrieve page views
user_id = "86226"

# Define start and end dates (in ISO 8601 format)
#start_date = "YYYY-MM-DDTHH:MM:SSZ"
start_datetime = "2024-03-22T00:00:00Z"
end_datetime = "2024-03-22T23:59:59Z"

# Convert start and end dates to datetime objects
#start_datetime = datetime.fromisoformat(start_date)
#end_datetime = datetime.fromisoformat(end_date)

# Get the user object
user = canvas.get_user(user_id)

# Retrieve page views for the user
page_views = user.get_page_views(start_time=start_datetime, end_time=end_datetime)

# Print page views details
with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile, dialect='excel')
    writer.writerow(["Session ID", "Context ID", "Page ID", "Context Type", "Controller", "Action", "HTTP Method","Page URL", "Viewed At", "Participated", "Real User", "Remote IP", "User Agent", "App Name"])
    for page_view in page_views:
        created_at_utc = datetime.strptime(page_view.created_at, "%Y-%m-%dT%H:%M:%S%z").replace(tzinfo=utc_timezone).astimezone(central_timezone)
        csvdata = (page_view.session_id, page_view.links['context'], page_view.id, page_view.context_type, page_view.controller, page_view.action, page_view.http_method, page_view.url, created_at_utc, page_view.participated,page_view.links['real_user'], page_view.remote_ip, page_view.user_agent, page_view.app_name)
        writer.writerow(csvdata)
        print("Session ID: ", page_view.session_id)
        print("Canvas Course ID: ", page_view.links['context'])
        # #print("Context ID: ", page_view.links.context)
        print("Context Type: ", page_view.context_type)
        print("Controller: ", page_view.controller)
        # print("Action: ", page_view.action)
        # print("HTTP Method: ", page_view.http_method)
        print("Page URL:", page_view.url)
        # print("Viewed At:", page_view.created_at)
        # print("Participated",page_view.participated)
        # #print("Page Title:", page_view.title)
        print("Remote IP:", page_view.remote_ip)
        # print("User Agent:", page_view.user_agent)
        # print("App Name:", page_view.app_name)
        print("--------------------------------------------------------------------------------")
