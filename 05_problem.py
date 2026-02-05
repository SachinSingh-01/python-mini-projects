'''Word Frequency Counter (File Based)
What to build
Find most repeated words in a text file.
Read a file
Split words
Count frequency using dictionary
Print top 5 most repeated words
Concepts used
file handling
string split
dictionary
loops'''
with open("repeated_words.txt","r") as file:
    content=file.read().split()
    dic={}
    for word in content:
        if word in dic:
            dic[word]+=1
        else:
            dic[word]=1
sorted_words = sorted(dic.items(), key=lambda x: x[1], reverse=True)
print("\nTop 5 most repeated words:\n")
for word, count in sorted_words[:5]:
    print(word, "→", count)
