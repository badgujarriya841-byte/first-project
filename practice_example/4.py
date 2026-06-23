# Question 4: Function to Count Vowels 
# Question: Create a function that accepts a string and returns the number of vowels (a, e, i, o, u) present in it. Print the count. 

def Count_vowel(text):
    count = 0
    for char in text.lower():
        if char in "a,e,i,o,u":
            count += 1
    return count

string = input("Enter a word: ")
print("Number of vowels = ",Count_vowel(string))