import model.Note
import model.Write.WriteToFile as wTf
import model.Write.LoadFromFile as lFf

def deleteNot():
    id = input("Enter the id of the note: ")
    array_notes = lFf.read_file()
    flag = False

    for i in array_notes:
        if id == model.Note.Note.get_id(i):
            array_notes.remove(i)
            flag = True

    if flag:
        wTf.write_file(array_notes, 'a')
        print("Note with id: ", id, " is deleted")
    else:
        print("No note with this id")