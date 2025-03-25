movies = []

def add_movie_list():
    movie = input("Enter your favourite movie: ").strip()
    if movie:
        movies.append(movie)
        movies.sort()
        print(f"'{movie}' has been added to your list.")
    else:
        print("Updated list:", movies)

def remove():
    dislike = input("Remove from list: ").strip()
    if dislike in movies:
        movies.remove(dislike)
        print(f"{dislike} has been deleted")
    else:
        print(f"'{dislike}' not found in the list.")


def main():
    while True:
        choice = input("1.Add movies: \n2.Which movie would you like to remove?\nchoice: ")
        if choice == "1":
            add_movie_list()
            print(movies)
        elif choice =="2" :
            remove()
            print(movies)
        else:
            break

main()
