from transformers import pipeline
import textstat

sentiment_analyzer = pipeline("sentiment-analysis")
text = input("Enter your text or writing: \n")

#split text to count words
words = text.split()
word_count = len(words)

#count sentences
sentences = text.split(".")
sentence_count = len(sentences)

#find the average sentence length
avg_sentence_length = word_count / sentence_count

result = sentiment_analyzer(text)

tone = result [0] ["label"]
confidence = result [0] ["score"]

readability = textstat.flesch_reading_ease(text)

print("\n*******************")
print("AI Writing Analyzer")
print("*******************")

print(f"Word count: {word_count}")
print(f"Average sentence length: {avg_sentence_length:.1f} words")

print(f"Tone: {tone}")
print(f"Confidence: {confidence:.2f}")

print(f"\nReadability score: {readability:.1f}")

#suggestions based on readability, tone and sentiment scores
suggestion = []

if avg_sentence_length > 20:
    if readability < 60:
        suggestion.append("Sentences are long and the text is hard to read. Consider splitting sentences and using simpler words.")
    else:
        suggestion.append("Sentences are long. You might want to split them to improve readability more.")
else:
    if readability < 60:
        suggestion.append("Sentences are concise, but the text is still a bit hard to read. Try using simpler words.")
    else:
        suggestion.append("Sentences are concise and the text is easy to read.")

if tone == "POSITIVE":
    suggestion.append("Positive and engaging tone!")
elif tone == "NEGATIVE":
    suggestion.append("Your tone may come off as harsh, consider softenting it.")
else:
    suggestion.append("Your tone is neutral, a good choice for formal writings.")

print("\nSuggestions:")
for s in suggestion:
    print("-" + s)