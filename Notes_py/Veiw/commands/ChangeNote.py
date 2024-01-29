import model.Note
import model.Write.WriteToFile as wTf
import model.Write.LoadFromFile as lFf

def change_note():
    id = input("Enter the id of the note: ")
    array_notes = lFf.read_file()
    flag = True
    array_notes_new = []
    for i in array_notes:
        if id == model.Note.Note.get_id(i):
            i.title = input("Chsnge title:\n")
            i.body = input("Chsnge body:\n")
            model.Note.Note.set_date(i)
            logic = False
        array_notes_new.append(i)

    if flag:
        wTf.write_file(array_notes_new, 'a')
        print("Note with id: ", id, " is changed!")
    else:
        print("No note with this id")