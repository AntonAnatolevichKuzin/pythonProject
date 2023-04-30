import datetime
class Note:
    def __init__(self, note_id, title, body):
        self.id = note_id
        self.title = title
        self.body = body
        self.created_time = datetime.datetime.now()
        self.last_modified_time = self.created_time

    def __str__(self):
        return f"ID: {self.id}\nTitle: {self.title}\nBody: {self.body}\nCreated: {self.created_time}\nLast Modified: {self.last_modified_time}"
