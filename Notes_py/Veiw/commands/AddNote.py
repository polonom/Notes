import model.Note
import model.Write.WriteToFile as wTf
import model.Write.LoadFromFile as lFf


def add_note():
    title = input("Input the title:\n")
    body = input("Input body of the note :\n")
    note = model.Note.Note(title=title, body=body)
    array_notes = lFf.read_file()
    for i in array_notes:
        if model.Note.Note.get_id(note) == model.Note.Note.get_id(i):
            model.Note.Note.set_id(note)
    array_notes.append(note)
    wTf.write_file(array_notes, 'a')
    print("Note is added")