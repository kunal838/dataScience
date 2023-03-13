

#Q7
import matplotlib.pyplot as plt


text = input("Enter a string: ").lower()


freq = {}
for char in text:
    if char.isalpha():
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1

# plot bar chart
plt.bar(freq.keys(), freq.values())
plt.xlabel("Alphabet")
plt.ylabel("Frequency")
plt.show()
