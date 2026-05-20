# Vowel or Consonant

char=input("enter character: ").lower()
vowels='aeiou'
if char in vowels:
    print(f'{char} is vowel')
else:
    print(f'{char} is consonant')