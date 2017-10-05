import nltk

class Analyzer():
    """Implements sentiment analysis."""

    def __init__(self, positives, negatives):
        """Initialize Analyzer."""

        # create positive and negative sets of words
        self.positives = set()
        self.negatives = set()

        # fill the sets with words found in respective files
        with open('positive-words.txt') as lines:
            for line in lines:
                if line.startswith(';') == False: # exclude comments
                    self.positives.add(line.strip())

        with open('negative-words.txt') as lines:
            for line in lines:
                if line.startswith(';') == False: # exclude comments
                    self.negatives.add(line.strip())


    def analyze(self, text):
        """Analyze text for sentiment, returning its score."""

        # break texts apart
        tokenizer = nltk.tokenize.TweetTokenizer()
        tokens = tokenizer.tokenize(text)

        # initialize score
        score = 0

        # check each word
        for word in tokens:
            #if word is positive increment score
            if word.lower() in self.positives:
                score = score + 1

            # if word is negative decrement score
            if word.lower() in self.negatives:
                score = score - 1

        return score
