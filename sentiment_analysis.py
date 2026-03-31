import string

# Text
text_list = [
    "But soft, what light through yonder window breaks, it is the east and Juliet is the sun.",
    "Good night, good night! Parting is such sweet sorrow.",
    "Something wicked this way comes.",
    "Out, out brief candle! Life is but a walking shadow.",
    "Is this a dagger which I see before me? I am afraid and full of doubt."
]

# Word lists
positive_words = ["good", "light", "sun", "sweet", "lovely", "life"]
negative_words = ["wicked", "sorrow", "shadow", "dagger", "afraid", "doubt"]

# Clean text
def clean(sentence):
    sentence = sentence.lower()
    sentence = sentence.translate(str.maketrans("", "", string.punctuation))
    return sentence.split()

# Sentiment check
def sentiment(sentence):
    words = clean(sentence)
    pos = 0
    neg = 0

    for word in words:
        if word in positive_words:
            pos += 1
        elif word in negative_words:
            neg += 1

    if pos > neg:
        return "POSITIVE"
    elif neg > pos:
        return "NEGATIVE"
    else:
        return "NEUTRAL"

# Counters
pos_count = 0
neg_count = 0
neu_count = 0

# Output
print("\nSHAKESPEARE SENTIMENT ANALYSIS\n")

for i, line in enumerate(text_list, 1):
    result = sentiment(line)
    print(f"{i}. {line}")
    print(f"   Sentiment: {result}\n")

    if result == "POSITIVE":
        pos_count += 1
    elif result == "NEGATIVE":
        neg_count += 1
    else:
        neu_count += 1

# Overall sentiment result
print("OVERALL RESULT:")
print(f"Positive: {pos_count}")
print(f"Negative: {neg_count}")
print(f"Neutral : {neu_count}")

if pos_count > neg_count:
    print("Overall Sentiment: POSITIVE")
elif neg_count > pos_count:
    print("Overall Sentiment: NEGATIVE")
else:
    print("Overall Sentiment of the text: NEUTRAL")
