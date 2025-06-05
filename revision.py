recipes = []      
def add_recipe(title, ingredients, steps):
    recipes.append({
        "title": title,
        "ingredients": ingredients,
        "steps": steps
    })
def search_recipes(query):
    words = query.lower().split()
    result = []
    for r in recipes:
        title = r["title"].lower()
        ing  = [i.lower() for i in r["ingredients"]]
        if all(any(w in field for field in [title, *ing]) for w in words):
            result.append(r)
    return result

add_recipe("Chapati", ["Flour", "Water", "Oil"], ["Mix", "Roll", "Fry"])
add_recipe("Fruit Salad", ["Mango", "Banana"], ["Chop", "Serve"])
print(search_recipes("flour")) 
print(search_recipes("mango"))
