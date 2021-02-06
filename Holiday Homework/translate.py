string = ("xqg eio nqfzy ioewwx poww aq yoa acfd uei pfac xqgi tiqyievvfzy. yqg cejo woeizon e wqa dfzko xqg hoyez oeiwfoi acfd xoei. xqgi drfwwd pfww nojowqt ugiacoi ed xqg daeia aq pifao xqgi qpz tiqyievd. kqzyieagweafqzd qz ojoixacfzy xqg cejo ekcfojon, xqg cejo aq ho joix tiqgn qu xqgidowu.")
encryption = input("\nWhat is the encryption?\n")

table = str.maketrans(string, "tzhsaiubrvcqjdewokxpfmlygn")

encrypt = string.translate(table)

print(encrypt)