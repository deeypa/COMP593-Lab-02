def main():
    # Step 2: Create a complex data structure
    about_me = {
        "full_name": "John Doe",
        "student_id": 987654321,
        "pizza_toppings": ["PEPPERONI", "MUSHROOMS", "ONIONS"],
        "movies": [
            {"title": "inception", "genre": "sci-fi"},
            {"title": "the dark knight", "genre": "action"}
        ]
    }

    # Step 3: Add another movie to the data structure
    about_me["movies"].append({"title": "interstellar", "genre": "sci-fi"})

    # Calling functions as per instructions
    print_student_name_and_id(about_me)
    print_pizza_toppings(about_me)
    add_pizza_toppings(about_me, ("BACON", "EXTRA CHEESE"))
    print_pizza_toppings(about_me)
    print_movie_genres(about_me)
    print_movie_titles(about_me["movies"])

# Step 4: Function that prints student name and ID
def print_student_name_and_id(about_me):
    first_name = about_me["full_name"].split()[0]
    print(f"My name is {about_me['full_name']}, but you can call me Sir {first_name}.")
    print(f"My student ID is {about_me['student_id']}.")

# Step 5: Function that adds pizza toppings to data structure
def add_pizza_toppings(about_me, toppings):
    about_me["pizza_toppings"].extend(toppings)
    about_me["pizza_toppings"] = sorted(t.lower() for t in about_me["pizza_toppings"])

# Step 6: Function that prints bullet list of pizza toppings
def print_pizza_toppings(about_me):
    print("My favourite pizza toppings are:")
    for topping in about_me["pizza_toppings"]:
        print(f"- {topping}")

# Step 7: Function that prints comma-separated list of movie genres
def print_movie_genres(about_me):
    genres = ", ".join(movie["genre"] for movie in about_me["movies"])
    print(f"I like to watch {genres} movies.")

# Step 8: Function that prints comma-separated list of movie titles
def print_movie_titles(movie_list):
    titles = ", ".join(movie["title"].title() for movie in movie_list)
    print(f"Some of my favourite movies are {titles}!")

if __name__ == '__main__':
    main()
