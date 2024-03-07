#Initialize empty list ,set ,and dictionary
books_list=[]
authors_set =set()
books_dict={}

#Add books
books_list.append("Python Programming")
authors_set.add ("John Smith")
books_dict["Python Programming"]="John Smith"

books_list.append("Data structure and Algorithms")
authors_set.add("Jane Doe")
books_dict["Data structure and Algorithms"]="Jane Doe"

books_list.append("Machine Learning Basic")
authors_set.add("Alices Johnson")
books_dict["Machine Learning Basic"]="Alices Johnson"

#Search for book
search_title=input("Enter the title of the book to search:")
if search_title in books_list:
    print(f"Book found! Author:{books_dict[search_title]} ")
else:
    print("Book not found!")

#Display all books 
print("list of books ")
for book in books_list:
    print(book)

#Remove a book 
remove_title=input("Enter the title of the book to remove or else enter the to skip:")
if remove_title in books_list:
    remove_author=books_dict[remove_title ]
    books_list.remove(remove_title)
    authors_set.remove(remove_author)
    del books_dict[remove_title]
    print("Bookremoved successfully!")
    print("Book available",books_list)

else:
    print("Book not found")

