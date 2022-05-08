from Time import DateTime
import datetime
from quickstart import Create_Service

CLIENT_SECRET_FILE = "client_secret.json"
API_NAME = "calendar"
API_VERSION = "v3"
SCOPES = ["https://www.googleapis.com/auth/calendar"]
Event_Names = []
Event_Times = []
Event_Dates = []

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

C_id = "danielgbrown2005@gmail.com"


def Get_Events(service):
    now = datetime.datetime.utcnow().isoformat() + "z"
    events_result = service.events().list(calendarId=C_id, timeMin=now, maxResults=10, singleEvents=True,
                                          orderBy="startTime").execute()
    events = events_result.get("items", [])
    if not events:
        print("null")
    for event in events:
        start = event["start"].get("dateTime", event["start"].get("date"))
        date, time = start.split("T", 1)
        time, discard = time.split("+", 1)
        Event_Names.append(event["summary"])
        Event_Times.append(time)
        Event_Dates.append(date)

Get_Events(service)


class Event:
    def __init__(self, index):
        self.name = Event_Names[index]
        self.date = Event_Dates[index]
        self.time = Event_Times[index]

    @staticmethod
    def next_event():
        if Event_Dates[0] == DateTime.return_current_date("google"):
            return f"You have a {Event_Names[0]} today at {Event_Times[0]}"
        else:
            return "You have nothing scheduled for today. "

    @staticmethod
    def tomorrows_event():
        for element in range(0, len(Event_Dates)):
            print(type(element))
            if Event_Dates[element] == DateTime.ChangeDate(1, "google"):
                return f"You have a {Event_Names[element]} tomorrow at {Event_Times[element]}"




