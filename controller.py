import text
import view
import model

def start():
    while True:
        choice = view.main_menu()
        match choice:
            case 1:
                model.pokaz()
            case 2:
                model.save()
                view.print_message(text.input_save)
            case 3:
                model.poisk()
            case 4:
                model.dobavlenie()
                view.print_message(text.input_dobavlen)
            case 5:
                model.izmenenie()
                view.print_message(text.izmenen)
            case 6:
                model.ydalenie()
                view.print_message(text.input_delete)
            case 7:
                break