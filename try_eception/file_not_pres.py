def readFile(filename):
    try:
        with open(filename, "r") as f:
            one = f.read()
            print(one)
    except FileNotFoundError:
        print(f"file {filename} does not exist")

readFile("one.txt")
readFile("two.txt")
readFile("three.txt")