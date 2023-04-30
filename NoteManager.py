import json
import datetime

from Note import Note


class NoteManager:
    def __init__(self, filename):
        self.filename = filename
        self.notes = []
        self.load_notes()

    def load_notes(self):
        try:
            with open(self.filename, "r") as f:
                data = json.load(f)
                for note_data in data:
                    note = Note(note_data["id"], note_data["title"], note_data["body"])
                    note.created_time = datetime.datetime.fromisoformat(note_data["created_time"])
                    note.last_modified_time = datetime.datetime.fromisoformat(note_data["last_modified_time"])
                    self.notes.append(note)
        except FileNotFoundError:
            pass

    def save_notes(self):
        with open(self.filename, "w") as f:
            data = []
            for note in self.notes:
                data.append({
                    "id": note.id,
                    "title": note.title,
                    "body": note.body,
                    "created_time": note.created_time.isoformat(),
                    "last_modified_time": note.last_modified_time.isoformat()
                })
            json.dump(data, f)

    def add_note(self, title, body):
        note_id = len(self.notes) + 1
        note = Note(note_id, title, body)
        self.notes.append(note)
        self.save_notes()
        return note_id

    def get_note_by_id(self, note_id):
        for note in self.notes:
            if note.id == note_id:
                return note
        return None

    def get_all_notes(self):
        return self.notes

    def update_note_by_id(self, note_id, title, body):
        note = self.get_note_by_id(note_id)
        if note is not None:
            note.title = title
            note.body = body
            note.last_modified_time = datetime.datetime.now()
            self.save_notes()
            return True
        else:
            return False

    def delete_note_by_id(self, note_id):
        note = self.get_note_by_id(note_id)
        if note is not None:
            self.notes.remove(note)
            self.save_notes()
            return True
        else:
            return False