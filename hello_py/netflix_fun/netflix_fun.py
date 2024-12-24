import csv

data = []

with open("data/netflix_titles.csv", newline="") as csvfile:
    reader = csv.DictReader(csvfile, delimiter=",", quotechar='"')
    csv_data = []
    for row in reader:
        row["cast"] = [st.strip() for st in row["cast"].split(",")]
        row["listed_in"] = [st.strip() for st in row["listed_in"].split(",")]
        csv_data.append(row)

    data = list(csv_data)


def head():
    print(data[1])


def last():
    print(data[len(data) - 1])


def indian_movies():
    print(list(filter(lambda d: d["country"] == "India", data)))


def movies_with_gary_oldman():
    movies = list(filter(lambda d: ("Gary Oldman" in d["cast"]), data))
    print(list(map(lambda m: m["title"], movies)))


def indian_comedies():
    indian_movies = list(filter(lambda d: d["country"] == "India", data))
    movies = list(filter(lambda d: ("Comedies" in d["listed_in"]), indian_movies))
    print(list(map(lambda m: m["title"], movies)))


def indian_movies_with_johnny_lever():
    indian_movies = list(filter(lambda d: d["country"] == "India", data))
    movies = list(filter(lambda d: ("Johnny Lever" in d["cast"]), indian_movies))
    print(list(map(lambda m: m["title"], movies)))
