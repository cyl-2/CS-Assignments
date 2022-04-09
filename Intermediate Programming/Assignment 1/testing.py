# books.py contains all the classes related to books
# testing.py is where I have my test block

from books import *

def testBlock():
    author1 = Author("Sarah O'Sullivan", "ABC Ent")
    author2 = Author("Conor Murphy", "XYZ Ent")

    #######################################################################

    book1 = RealBooks("Out And About", 5.08, 3.99)
    book1.author = author1
    
    print(book1)                        # prints full details of the book
    print(book1.getPrice())             # only prints the price of the book
    print(book1.getTitle())             # only prints the title of the book
    print(book1.getCost())              # only prints the total cost of that book (price + postage)
    print(book1.getAuthor())            # prints the full details of author 
    
    print("\n")

    #######################################################################

    book2 = EBooks("In And About", 10.16, "www.url1.com")
    # I'm not going to assign an author to book 2, so that my error message is printed out
    print(book2)
    print(book2.getTitle(), book2.getPrice(), book2.getURL(), sep = " || ")             # The title, price and URL of the book can still be fetched but a full detailed 
                                                                                            # report of the book won't be printed unless an author is assigned.
    print("\n")
    #######################################################################

    book3 = EBooks("Far Far Away", 55, "www.url2.com")
    book3.author = author2

    print(book3)                        # prints full details of the book
    print(book3.getPrice())             # only prints the price of the book
    print(book3.getTitle())             # only prints the title of the book
    print(book3.getURL())               # only prints the url of that book
    print(book3.getAuthor())            # prints the full details of author

    print("\n")

    #######################################################################

    book4 = RealBooks("Very Close", 1.01, 3)
    book4.author = author2

    print("Book 4 author: ", book4.getAuthor(), "Book 3 author: ", book3.getAuthor(), sep = "\n\n") # book 3 and book 4 have the same author because one author can write many books

    #######################################################################

if __name__ == "__main__":
    testBlock()