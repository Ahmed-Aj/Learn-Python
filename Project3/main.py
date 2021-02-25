class Author:
    def __init__(self, name, lastname):
        self.Name = name
        self.LastName = lastname

    def ShowAuthor(self):
        print("Author: ", self.Name, " ", self.LastName)


class Book:
    def __init__(self, title, isbn):
        self.Title = title
        self.ISBN = isbn

    def AddAuthor(self, author):
        self.Author = author

    def ShowBook(self):
        print("-----Books-----")
        print("Title: ", self.Title)
        print("ISBN: ", self.ISBN)
        self.Author.ShowAuthor()
        print("---------------")

    def GetTitle(self):
        return self.Title


class Library:
    def __init__(self):
        self.BookList = []

    def NumberOfBooks(self):
        return len(self.BookList)

    def AddBook(self, book):
        self.BookList = self.BookList + [book]

    def ShowLibrary(self):
        print("----------------------")
        for item in self.BookList:
            return item.ShowBook()
        print("----------------------")

    def DeleteBook(self, title):
        found = False
        position_to_delete = -1
        for item in self.BookList:
            position_to_delete = position_to_delete + 1
            if item.GetTitle() == title:
                found = True
                break
        if found:
            del self.BookList[position_to_delete]
            print("Book is deleted. ")
        else:
            print("Book not found. ")


def ShowMenu():
    print("""MENU...
1) Add Books to the library.
2) Show the library.
3) Delete a book from the library.
4) Show the number of books that make up the library.
5) Exit.""")


def AddBookToLibrary(library):
    title = input("Enter the book name: ")
    isbn = input("Enter the ISBN of the book: ")
    author_name = input("Enter the first name of the author: ")
    author_l_name = input("Enter the last name of the author: ")
    author = Author(author_name, author_l_name)
    book = Book(title, isbn)
    book.AddAuthor(author)
    library.AddBook(book)
    return library


def ShowLibrary(library):
    library.ShowLibrary()


def DeleteBookFronLibrary(library):
    title = input("Enter the title of the book to delete: ")
    library.DeleteBook(title)


def NumberOfBooks(library):
    print("The number of books: ", library.NumberOfBooks())


end = False
library = Library()

while not end:
    ShowMenu()

    option = int(input("Option: "))
    if option == 1:
        library = AddBookToLibrary(library)
    elif option == 2:
        ShowLibrary(library)
    elif option == 3:
        DeleteBookFronLibrary(library)
    elif option == 4:
        NumberOfBooks(library)
    elif option == 5:
        end = True

print("Thank you for shopping, Goodbye!!!!!!")
