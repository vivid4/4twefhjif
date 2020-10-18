from tkinter import *
from tkinter import ttk

# GUI CODING
root = Tk()
root.title("Comic Book Store")
root.geometry("460x600") # the size of the window




# CLASS CODE FOR BOOKS
class Book:
    """The Book class stores the details of each book in the comic book store and has methods of purchasing, restocking and viewing details"""
    def __init__(self, title, amount, sold):
        self.title = title
        self.amount = amount
        self.sold = sold
        book_list.append(self)

    #Purchasing book
    def purchase(self):
        if self.amount > 0:
            self.amount -= 1
            return True
        else:
            return False

    #Restocking book
    def restock(self, number):
        if number > 0:
            self.amount += number
            return True
        else:
            return False

#create function for book names list
def book_names_list():
    name_list = []
    for book in book_list:
        name_list.append(book.title)
    return name_list




#****edit/fix this code**** ---> function updating the text
def update_book_details():
    for book in book_list:
        amount = book.get_amount()
        pass
    
    book_details_string = StringVar()
    book_details_string = "Super Dude: {}\nLizard Man: {}\nWater Woman: {}".format()
    book_details.set(book_details_string)
    number.set("")




#set up list
book_list = []

# instances of the class
super_dude = Book("Super Dude", 8)
lizard_man = Book("Lizard Man", 12)
water_woman = Book("Water Woman", 3)

# name list command
book_names = book_names_list()




#---welcome frame / 'Comic Book Store' LabelFrame
welcome_container = ttk.LabelFrame(root, text="Comic Book Store", padding=20)
welcome_container.grid(column=0, row=0, sticky="WE", padx=100, pady=10)
welcome_text = StringVar()
welcome_text.set("""Welcome to the Comic Book Store!

Our books that are currently in stock and amount of books sold:""")
welcome_label = ttk.Label(welcome_container, textvariable=welcome_text, wraplength=200)
welcome_label.grid(column=0, row=0, columnspan=2, padx=10, pady=10)

#book details
book_details = StringVar()
book_details.set("Super Dude: 8\nLizard Man: 12\nWater Woman: 3")
book_details_label = ttk.Label(welcome_container, textvariable=book_details)
book_details_label.grid(column=0, row=1, padx=10, pady=10)

# number of books sold
sold_details = StringVar()
sold_details.set("Books sold: 0\nBooks sold: 0\nBooks sold: 0")
sold_details_label = ttk.Label(welcome_container, textvariable=sold_details)
sold_details_label.grid(column=1, row=1, padx=10, pady=10)






#---option frame
option_container = ttk.LabelFrame(root, text="Book Details", padding=20)
option_container.grid(column=0, row=1, sticky="WE", padx=100, pady=10)
option_text = ttk.Label(option_container, text="Please select a book and option.")
option_text.grid(column=0, row=0, padx=10, pady=10)

#select book
selected_book = StringVar()
selected_book.set(book_names[0])
books_combobox = ttk.Combobox(option_container, textvariable=selected_book, state="readonly")
books_combobox['values'] = book_names
books_combobox.grid(column=0, row=2, padx=5, pady=5, sticky="WE")

#store the number
number = DoubleVar()
number.set("")

#option entry/type number
option_entry = ttk.Entry(option_container, textvariable=number, state="normal")
option_entry.grid(column=0, row=3, padx=5, pady=5, sticky="WE")



#Purchase button
confirmation_button = ttk.Button(option_container, text="Purchase", command=update_book_details)
confirmation_button.grid(column=1, row=2, columnspan=1, padx=10, pady=10)

#Restock button
confirmation_button = ttk.Button(option_container, text="Restock", command=update_book_details)
confirmation_button.grid(column=1, row=3, columnspan=1, padx=10, pady=10)


#---mainloop
root.mainloop()
