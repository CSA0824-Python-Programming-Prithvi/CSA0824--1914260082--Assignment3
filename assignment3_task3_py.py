import string

calls = [
    "seeds not received seeds delayed",
    "fertiliser price high",
    "seeds price high subsidy not received"
]

STOP = {"not", "high"}

def frequencies(texts, stop):
    counts = {}

    for text in texts:
        text = text.lower()

        for word in text.split():
            word = word.strip(string.punctuation)

            if word and word not in stop:
                counts[word] = counts.get(word, 0) + 1

    return counts

def top(counts, k):
    return sorted(counts.items(),
                  key=lambda x: (-x[1], x[0]))[:k]

print(top(frequencies(calls, STOP), 3))
