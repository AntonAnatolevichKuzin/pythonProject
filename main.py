import argparse

from NoteManager import NoteManager

parser = argparse.ArgumentParser(description='Note taking app')
parser.add_argument('command', choices=['add', 'list', 'view', 'update', 'delete'], help='command to execute')
parser.add_argument('--id', type=int, help='note id')
parser.add_argument('--title', help='note title')
parser.add_argument('--body', help='note body')

args = parser.parse_args()

note_manager = NoteManager('notes.json')

if args.command == 'add':
    note_id = note_manager.add_note(args.title, args.body)
    print(f"Note added with ID: {note_id}")
elif args.command == 'list':
    notes = note_manager.get_all_notes()
    for note in notes:
        print(note)
        print()
elif args.command == 'view':
    note = note_manager.get_note_by_id(args.id)
    if note is not None:
        print(note)
    else:
        print(f"Note with ID {args.id} not found.")
elif args.command == 'update':
    if note_manager.update_note_by_id(args.id, args.title, args.body):
        print(f"Note with ID {args.id} updated.")
    else:
        print(f"Note with ID {args.id} not found.")
elif args.command == 'delete':
    if note_manager.delete_note_by_id(args.id):
        print(f"Note with ID {args.id} deleted.")
    else:
        print(f"Note with ID {args.id} not found.")