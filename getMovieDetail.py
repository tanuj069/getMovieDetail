import imdb                                         # importing the module
hr = imdb.IMDb()                                    # creating instance of IMDb
movie_name = input("Enter the name of movie: ")     # movie name
movies = hr.search_movie((str(movie_name)))         # searching the movie

choice = input("Want the all movies related to that name -> (Y/N): ")
print("If you also want to know the cast of any particular movie, then press 'Y', otherwise 'N', just immediately after the movie name visible to you: ")
index = movies[0].getID()
movie = hr.get_movie(index)
title = movie['title']
year = movie['year']
print(title, "(", year, ")")
ch = input()
if ch == 'Y' or ch == 'y':
    cast = movie['cast']
    list_of_cast = ','.join(map(str, cast))
    print("full cast: ", list_of_cast)


if choice == 'Y' or choice == 'y':
    k = 1
    for i in movies:
        index = movies[k].getID()
        movie = hr.get_movie(index)
        year = movie['year']
        print(i, "(", year, ")")
        ch = input()
        if ch == 'Y' or ch == 'y':
            cast = movie['cast']
            list_of_cast = ','.join(map(str, cast))
            print("full cast: ", list_of_cast)
        k += 1