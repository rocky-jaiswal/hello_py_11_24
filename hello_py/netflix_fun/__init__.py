import argparse

from .netflix_fun import *


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("positional_arg")
    parser.add_argument("--optional_flag", default="default_value")
    args = parser.parse_args()

    match f"{args.positional_arg}":
        case "head":
            head()
        case "last":
            last()
        case "indian_movies":
            indian_movies()
        case "movies_with_gary_oldman":
            movies_with_gary_oldman()
        case "indian_movies_with_johnny_lever":
            indian_movies_with_johnny_lever()


if __name__ == "__main__":
    main()
