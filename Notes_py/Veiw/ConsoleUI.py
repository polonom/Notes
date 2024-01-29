import Veiw.commands.AddNote as aNote
import Veiw.commands.ChangeNote as cNote 
import Veiw.commands.DeleteNote as dNote 
import Veiw.commands.ShowNote as sNote

def start():
    while True:
       print("Hi.Choose what do u want to do with a note")
       print("\n 1.Add note")
       print("\n 2.Show all notes")
       print("\n 3.Delete note")
       print("\n 4.Change note")
       print("\n 5.Show note on specific date")
       print("\n Enter number of the command")
       numb = input()
       if numb == '1':
            aNote.add_note()
       elif numb == '2':
            sNote.show("all")
       elif numb == '3':
            dNote.deleteNot()
       elif numb == '4':
            cNote.change_note()
       elif numb == '5':
            sNote.show("date")
       else:
            print("Program is done")
            break
            

    
            



    
     