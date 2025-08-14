def get_books_from_user():
    books = []
    n = int(input("How many books do you want to enter? "))
    for i in range(n):
        title = input(f"Enter the title of book {i+1}: ")
        genre = input(f"Enter the genre of '{title}': ")
        books.append({'title': title, 'genre': genre})
    return books

def recommend_books(books, preferred_genre):
    recommended = [book['title'] for book in books if book['genre'].lower() == preferred_genre.lower()]
    return recommended

if __name__ == "__main__":
    books = get_books_from_user()
    preferred_genre = input("Enter your preferred genre: ")
    recommendations = recommend_books(books, preferred_genre)
    if recommendations:
        print("Recommended books in your preferred genre:")
        for title in recommendations:
            print("-", title)
    else:
        print("No books found in your preferred genre.")
