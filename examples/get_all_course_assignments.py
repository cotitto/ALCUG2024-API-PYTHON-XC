# Import the Canvas class
from canvasapi import Canvas
import csv
from datetime import datetime
import os

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

def gt_output_filename():
    now = datetime.now()
    yr= now.strftime("%Y")
    mo= now.strftime("%m")
    day=now.strftime("%d")
    fname = 'All_Assignments_'+str(yr)+'_'+str(mo)+'_'+str(day)+'.csv'

    return fname

filename = gt_output_filename()
print(filename)

course = canvas.get_course(72665) #Add Canvas Course ID
print("Selected course: \n", course.name)
assignments = course.get_assignments()

with open(filename,'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile,dialect='excel')
    writer.writerow(["Assigment ID", "Assigment Name", "Status", "Description", "Points", "Due Date"])
    for assignment in assignments:
        print(assignment)

        #print(external_tool)
        csvdata = (assignment.id, assignment.name, assignment.workflow_state, assignment.description, assignment.points_possible, assignment.due_at)
        writer.writerow(csvdata)

        print('Finished processing assignment: ', assignment)
        print('#'*150)