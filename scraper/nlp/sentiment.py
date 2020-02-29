from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


def init():
    analyzer = SentimentIntensityAnalyzer()
    return analyzer


def polarity(analyzer, text):
    return analyzer.polarity_scores(text)['compound']
