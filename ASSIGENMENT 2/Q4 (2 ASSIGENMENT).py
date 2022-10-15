String="Sujal Mansuri 16-03-2004"

list = list(filter(lambda x: True if x in "0123456789" else False, String))

print(list)