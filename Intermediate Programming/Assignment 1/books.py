# books.py contains all the classes related to books
# testing.py is where I have my test block

class Author(object):
    # The class Author contains the name of the author and the publisher of the book
    def __init__(self, name, publisher):
        self._name = name
        self._publisher = publisher

    # Returns string with the details of the author when the author class is called
    def __str__(self):
        return "Author details: \nName: %s \nPublisher: %s" % (self._name, self.publisher)

    # getters and setters for both the author name + publisher of the book
    def getAuthorName(self):
        return self._name

    def setAuthorName(self):
        self._name = name

    def getAuthorPublisher(self):
        return self._publisher
    
    def setAuthorPublisher(self):
        self._publisher = publisher

    # setting the author name and publisher as properties 
    name = property(getAuthorName, setAuthorName)
    publisher = property(getAuthorPublisher, setAuthorPublisher)

class Books(object):
    # title and price are attributes of the books
    def __init__(self, title, price):
        self._title = title
        self._price = price
        self._author = None     # there is no author for now in the Books class, but an author will be assigned to each book later in the test block

    # setting getters for the book title + price
    def getTitle(self):
        return self._title

    def getPrice(self):
        return ("€%.2f" % (self._price))
    
    # setting a getter and a setter for author details
    def getAuthor(self):
        return self._author

    def setAuthor(self, author):
        self._author = author

    # declaring the book title + book price + author details as properties
    title = property(getTitle)
    price = property(getPrice)
    author = property(getAuthor, setAuthor)

class RealBooks(Books):
    # RealBooks is a child class of "Books"
    def __init__(self, title, price, postage):
        # It inherits the book title, price and author from the parent class "Books"
        super().__init__(title, price)
        # RealBooks doesn't inherit the postage price from the parent, so that is added below
        self._postage = postage

    # Returns string containing details of this "real" book
    def __str__(self):
        if self._author == None:
            return "Please assign an author and publisher to this book. All books must be written by an author and published by a publisher."
        else:
            euro = "€"
            cost = self._postage + self._price  # to calculate total cost of a book, which is price + postage fee
            return ("Title:%s \tPrice:%s%.2f \tAuthor Name:%s \tPublisher:%s \tPostage:%s%i \tTotal cost: %s%.2f" % (self._title, euro, self._price, self._author.name, self._author.publisher, euro, self._postage, euro, cost))

    def getPostage(self):
        return self._postage

    def getCost(self):
        return ("€%.2f" % (self._postage + self._price))
        
    postage = property(getPostage)
    cost = property(getCost)

class EBooks(Books):
    # EBooks is also a child class of "Books"
    def __init__(self, title, price, url):
        # It inherits the book title, price and author from the parent
        super().__init__(title, price)
        # It doesn't inherit the URL from the parent, so I added that below
        self._url = url

    # Returns string containing details of this book
    def __str__(self):
        if self._author == None:
            return "Please assign an author and publisher to this book. All books must be written by an author and published by a publisher."
        else:
            euro = "€"
            return ("Title:%s \tPrice:%s%.2f \tAuthor Name:%s \tPublisher:%s \tURL:%s \tTotal cost: %s%.2f" % (self._title, euro, self._price, self._author.name, self._author.publisher, self._url, euro, self._price))

    def getURL(self):
        return self._url

    url = property(getURL)