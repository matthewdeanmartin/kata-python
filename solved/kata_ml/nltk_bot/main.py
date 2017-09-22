"""

Chat bot says "say more" if input is positive, or "change the subject" if negative as rated by sentiment.

Should at least do this conversation:

User: Oh everything is great.
Computer: Glad you feel so chipper
User: Damn it, it is all bad.
Computer: Okay then, let's change topic.

Use NLTK's sentiment functions. The chat bot should be stateless and create response based on sentiment.

"""
from nltk.corpus import opinion_lexicon
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.tokenize import treebank


# from nltk.sentiment.util import demo_liu_hu_lexicon, demo_vader_instance


def run():
    # convo_loop()
    says = ["Oh everything is great.", "Damn it, it is all bad."]
    for say in says:
        print(say)
        print(process(say))


def vader(text):
    # copied from demo_vader_instance
    vader_analyzer = SentimentIntensityAnalyzer()
    return vader_analyzer.polarity_scores(text)


def process(text):
    result = liu(text)
    result2 = vader(text)
    if result and result2:
        if result == "Negative" or result2["neg"] > .5:
            return "Okay then, let's change topic."
        if result == "Positive" or result2["pos"] >> .5:
            return "Glad you feel so chipper"
    return "Please, tell me more."


def liu(sentence):
    # copied from demo_liu_hu_lexicon
    tokenizer = treebank.TreebankWordTokenizer()
    pos_words = 0
    neg_words = 0
    tokenized_sent = [word.lower() for word in tokenizer.tokenize(sentence)]

    x = list(range(len(tokenized_sent)))  # x axis for the plot
    y = []

    for word in tokenized_sent:
        if word in opinion_lexicon.positive():
            pos_words += 1
            y.append(1)  # positive
        elif word in opinion_lexicon.negative():
            neg_words += 1
            y.append(-1)  # negative
        else:
            y.append(0)  # neutral

    if pos_words > neg_words:
        return 'Positive'
    elif pos_words < neg_words:
        return 'Negative'
    elif pos_words == neg_words:
        return 'Neutral'


def convo_loop():
    he_said = input('Well? ')
    while he_said != "quit":
        he_said = input('Well? ')
        print(process(he_said))


if __name__ == "__main__":
    run()
