import streamlit as st
from collections import Counter


# Generate N-Grams from a sentence
def generate_ngrams(sentence, n):
    words = sentence.lower().split()

    ngrams = []

    for i in range(len(words) - n + 1):
        ngram = tuple(words[i:i + n])
        ngrams.append(ngram)

    return ngrams


# Calculate similarity using Dice similarity
def calculate_similarity(ngrams1, ngrams2):
    count1 = Counter(ngrams1)
    count2 = Counter(ngrams2)

    common = sum((count1 & count2).values())
    total = sum(count1.values()) + sum(count2.values())

    if total == 0:
        return 0.0

    return (2 * common / total) * 100


# Website title
st.title("TextMatch: N-Gram Text Similarity Analyzer")

st.write(
    "Compare two sentences using Unigrams, Bigrams, "
    "and Trigrams."
)

# Input sentences
sentence1 = st.text_area(
    "Enter the First Sentence",
    "I love learning Python"
)

sentence2 = st.text_area(
    "Enter the Second Sentence",
    "I love learning Java"
)

# Select N-Gram type
ngram_type = st.selectbox(
    "Choose N-Gram Type",
    ["Unigram", "Bigram", "Trigram"]
)

# Map the selected type to N
n = {
    "Unigram": 1,
    "Bigram": 2,
    "Trigram": 3
}[ngram_type]

# Compare button
if st.button("Compare Text"):
    if not sentence1.strip() or not sentence2.strip():
        st.warning("Please enter both sentences.")

    else:
        ngrams1 = generate_ngrams(sentence1, n)
        ngrams2 = generate_ngrams(sentence2, n)

        st.subheader("N-Gram Analysis")

        st.write("Sentence 1 N-Grams:")
        st.write([" ".join(x) for x in ngrams1])

        st.write("Sentence 2 N-Grams:")
        st.write([" ".join(x) for x in ngrams2])

        # Find matching patterns
        common = Counter(ngrams1) & Counter(ngrams2)
        matching = list(common.elements())

        st.subheader("Matching Word Patterns")

        if matching:
            st.write([" ".join(x) for x in matching])
        else:
            st.write("No matching N-Grams found.")

        # Calculate similarity
        similarity = calculate_similarity(
            ngrams1, ngrams2
        )

        st.subheader("Similarity Score")
        st.progress(int(similarity))
        st.write(f"Similarity: {similarity:.2f}%")

        st.caption(
            "The score measures overlap between N-Gram patterns. "
            "It does not measure the full meaning of the sentences."
        )

