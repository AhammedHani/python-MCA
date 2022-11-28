list = [22, 7, -9, 1, -4, 5]
newlist = [x for x in list if x < 0]
print(newlist)

sq = [x * x for x in list]
print(sq)

vowels = ['a', 'e', 'i', 'o', 'u']
str = input("Enter a string: ")
vowel_list = [x for x in str if x in vowels]
print(vowel_list)

ord_list = [ord(x) for x in str]
print(ord_list)
