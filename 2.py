class Book:
    def __init__(self, title, author):
        self.title = title  
        self.author = author 

    def short_title(self):  
        return self.title[:10]


book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
book2 = Book("To Kill a Mockingbird", "Harper Lee")
book3 = Book("Pride and Prejudice", "Jane Austen")


print(f"Short title of '{book1.title}': {book1.short_title()}")
print(f"Short title of '{book2.title}': {book2.short_title()}")
print(f"Short title of '{book3.title}': {book3.short_title()}")
