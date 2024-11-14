#Initialize an Empty List.
#Prompt the User for Input.
#Store the Books in the List.
#Sort the List
#Print the Sorted List

fave_books=[]

top3=(input('What are your top 3 favorite books?'))

fave_books.insert(2,top3)

fave_books.sort()
print(fave_books)