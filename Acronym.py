def main():
    phrase = input("Enter a phrase: ")

    words = phrase.split()
    acronym = ""

    for word in words:
        acronym = acronym + word[0]

    print("The acronym is:", acronym.upper())


if __name__ == "__main__":
    main()
