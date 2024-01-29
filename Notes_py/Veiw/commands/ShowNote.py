import model.Note
import model.Write.WriteToFile as wTf
import model.Write.LoadFromFile as lFf

def show(txt):
    array_notes = lFf.read_file()

    if array_notes:
        if txt == "all":
            for i in array_notes:
                print(model.Note.Note.map_note(i))

        elif txt == "date":
            date = input("Enter the date: dd.mm.yyyy: ")
            flag = True
            for i in array_notes:
                date_note = str(model.Note.Note.get_date(i))
                if date == date_note[:10]:
                    print(model.Note.Note.map_note(i))
                    flag = False
            if flag:
                print("Нет такой даты")
        else:
            print("Журнал заметок пустой!")
