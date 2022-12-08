text = "Надо удабвлить все слова с послабвостью абв и только их, вот так!"
# Separate punctuation marks with spaces in order to save them from deletion:
lst = text.replace(".", " .").replace(",", " ,")\
           .replace("?", " ?").replace("!", " !").split(" ")
corrected = filter(lambda s: s.find("абв") == -1, lst)
result = " ".join(corrected)
# bring back punctuation marks:
result = result.replace(" .", ".").replace(" ,", ",")\
           .replace(" ?", "?").replace(" !", "!")
print(result)
