#list1 = ["hello", "my", "name", "is", "python"]
def remove_and_strip(this, word):
    new_str = this.replace(word, "")
    str1 = new_str.strip()
    return str1

this = "     Hello this is python string"
word = "python"
#w = this.strip()
w = remove_and_strip(this, word)
print(w)