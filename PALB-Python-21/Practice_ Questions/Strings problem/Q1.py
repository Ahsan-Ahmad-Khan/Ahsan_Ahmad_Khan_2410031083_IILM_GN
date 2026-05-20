"""
Write a program to count:
    - Number of vowels
    - Number of consonants
Ignore digits and special characters.
"""
str=input("enter string: ")
vowel_count=0
consonant_count=0
for ch in str:
    if ch.isalpha():
        if ch.lower() in "aeiou":
            vowel_count+=1
        else:
            consonant_count+=1
    else:
        print("Invalid character")
print(vowel_count,consonant_count)


