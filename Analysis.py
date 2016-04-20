from textblob import TextBlob
import matplotlib.pyplot as plt
from textblob.sentiments import NaiveBayesAnalyzer
from textblob.classifiers import NaiveBayesClassifier

def get_pos_neg_distrib(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        analyser = NaiveBayesAnalyzer()
        # classifier = NaiveBayesClassifier()
        negative = 0
        positive = 0
        # positive_value = 0
        # negative_value = 0
        # count =0
        for line in lines:
            if len(line.split()) > 2:
                tweet = TextBlob(line, analyzer=analyser)#, classifier=classifier)
                # positive_value += tweet.sentiment.p_pos
                # negative_value += tweet.sentiment.p_neg
                # count+=1
                if tweet.sentiment.classification =='pos':
                    positive += 1
                # elif tweet.classify() =='neg':
                elif tweet.sentiment.classification =='neg':
                    negative += 1
    f.close()
    return positive, negative


def main():
    clinton_pos, clinton_neg = get_pos_neg_distrib('unique_clinton_tweets.txt')
    # print clinton_pos
    # print clinton_neg

    plt.figure(0)
    plt.pie([clinton_pos, clinton_neg],
            colors=["green", "red"],
            labels=["clinton_pos", "clinton_neg"],
            autopct='%1.1f%%',
            startangle=90)
    plt.axis('equal')

    trump_pos, trump_neg = get_pos_neg_distrib('unique_trump_tweets.txt')

    plt.figure(1)
    plt.pie([trump_pos, trump_neg],
            colors=["yellow", "blue"],
            labels=["trump_pos", "trump_neg"],
            autopct='%1.1f%%',
            startangle=90)

    plt.axis('equal')  # ensure pie is round
    plt.show()



if __name__ == '__main__':
    main()
