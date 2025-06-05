from textblob import TextBlob
sentence = input("Enter a sentence")
blob = TextBlob(sentence)
sentiment = blob.sentiment.polarity
if sentiment > 8:
 print("positive")
elif sentiment < 0:
 print("negative")
else:
 print("neutral")