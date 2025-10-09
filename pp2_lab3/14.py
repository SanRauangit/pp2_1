movies = [
    {"name": "Usual Suspects", "imdb": 7.0, "category": "Thriller"},
    {"name": "Hitman", "imdb": 6.3, "category": "Action"},
    {"name": "Dark Knight", "imdb": 9.0, "category": "Adventure"},
    {"name": "The Help", "imdb": 8.0, "category": "Drama"},
    {"name": "The Choice", "imdb": 6.2, "category": "Romance"},
    {"name": "Colonia", "imdb": 7.4, "category": "Romance"},
    {"name": "Love", "imdb": 6.0, "category": "Romance"},
    {"name": "Bride Wars", "imdb": 5.4, "category": "Romance"},
    {"name": "AlphaJet", "imdb": 3.2, "category": "War"},
    {"name": "Ringing Crime", "imdb": 4.0, "category": "Crime"},
    {"name": "Joking muck", "imdb": 7.2, "category": "Comedy"},
    {"name": "What is the name", "imdb": 9.2, "category": "Suspense"},
    {"name": "Detective", "imdb": 7.0, "category": "Suspense"},
    {"name": "Exam", "imdb": 4.2, "category": "Thriller"},
    {"name": "We Two", "imdb": 7.2, "category": "Romance"}
]
n=int(input("Movie database functions: \n 1.If movie is high rated  \n 2.All high rated movies(IMDB>5.5) \n 3.Movies by category \n 4.Average IMDB score of a list of movies \n 5.Average IMDB score of a category movies \n"))
if(n==1):
    # 1
    def is_high_rated(movie):
        return movie["imdb"] > 5.5
    n=int(input())
    test=movies[n]
    print(is_high_rated(test))
elif(n==2):
    # 2
    def get_high_rated_movies(movie_list):
        print( [movie for movie in movie_list if movie["imdb"] > 5.5])
    get_high_rated_movies(movies)
elif(n==3):
    # 3
    def get_movies_by_category(movie_list,category):
        return [movie for movie in movie_list if movie["category"].lower()==category.lower()]
    c=input("Enter category: ")
    print(get_movies_by_category(movies,c))
elif(n==4):
    # 4
    def average_imdb_score(movie_list, title=""):
        if not movie_list:
            print(f"No movies found for '{title}'")
            return
    
        print(f"\n{title}:")
        print("-" * 50)
        for i, movie in enumerate(movie_list, 1):
            print(f"{i}. {movie['name']} - IMDB: {movie['imdb']} - Category: {movie['category']}")
        print("-" * 50)
        total_score = sum(movie["imdb"] for movie in movie_list)
        average = total_score / len(movie_list)
        return average
    average_imdb_score(movies,"All available movies")
            
    custom_list = []
    while True:
        try:
                    movie_num = input("\nEnter movie number to add (or 'done' to finish): ").strip()
                    if movie_num.lower() == 'done':
                        break
                    
                    movie_num = int(movie_num)
                    if 1 <= movie_num <= len(movies):
                        custom_list.append(movies[movie_num - 1])
                        print(f"Added: {movies[movie_num - 1]['name']}")
                        print(f"Current list: {len(custom_list)} movies")
                    else:
                        print("Invalid movie number!")
                        
        except ValueError:
                print("Please enter a valid number or 'done'")
            
    if custom_list:
            avg_score = average_imdb_score(custom_list)
            print(f"\nAverage IMDB score of your custom list: {avg_score}")
            average_imdb_score(custom_list, "Your Custom Movie List")
    else:
            print("No movies selected!")
elif(n==5):
    # 5
    def average_imdb_by_category(movie_list,category):
        category_movies=get_movies_by_category(movie_list,category)
        return average_imdb_score(category_movies)
    def get_movies_by_category(movie_list,category):
        return [movie for movie in movie_list if movie["category"].lower()==category.lower()]
    n=input("Enter category: ")
    print(average_imdb_by_category(movies,n))
else:
    print("Please enter a valid number")