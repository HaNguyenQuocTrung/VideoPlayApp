from library_item import LibraryItem

# Initialize the library with items
library = {}
library["01"] = LibraryItem("Nightfall", "SoulProdMusic", 5, "Future Bass", "Future", "nightfall.mp3")
library["02"] = LibraryItem("Goodnight", "FASSounds", 4, "Advertisement", "Cold", "goodnight.mp3")
library["03"] = LibraryItem("Sunshine", "lemonmusicstudio", 4, "Classic", "Summer", "sunshine.mp3")
library["04"] = LibraryItem("Powerful", "MarkJuly", 4, "Blues", "Charm", "Powerful.mp3")
library["05"] = LibraryItem("Joyful", "Neura-Flow", 5, "Pop", "Optimistic", "Joyful.mp3")


def list_all():
    output = ""
    for key in library:
        item = library[key]
        output += f"{key} {item.info()}\n"
    return output

def get_name(key):
    try:
        item = library[key]
        return item.name
    except KeyError:
        raise KeyError(f"Key '{key}' not found in the library.")

def get_director(key):
    try:
        item = library[key]
        return item.director
    except KeyError:
        return None

def get_type(key):
    try:
        item = library[key]
        return item.type
    except KeyError:
        return None

def get_tempo(key):
    try:
        item = library[key]
        return item.tempo
    except KeyError:
        return None

def get_rating(key):
    try:
        item = library[key]
        return item.rating
    except KeyError:
        return -1

def set_rating(key, rating):
    try:
        item = library[key]
        item.rating = rating
    except KeyError:
        return

def get_play_count(key):
    try:
        item = library[key]
        return item.play_count
    except KeyError:
        return -1

def increment_play_count(key):
    try:
        item = library[key]
        item.play_count += 1
    except KeyError:
        return

def reset_play_count(key):
    try:
        item = library[key]
        item.play_count = 0
    except KeyError:
        return

def get_mp3_file(key):
    try:
        item = library[key]
        return item.mp3_file
    except KeyError:
        return None
