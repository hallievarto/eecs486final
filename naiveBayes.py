import sys
import os
from preprocess import tokenizeText

def trainNaiveBayes(fileList, dataset):
    androidCount = 0
    iphoneCount = 0
    androidWords = 0
    iphoneWords = 0
    wordCounts = {}
    V = 0
    for file in fileList:
        true = 0
        if 'android' in file:
            androidCount+=1
        else:
            iphoneCount+=1
            iphone = 1 
        f = open(dataset + '/' + file, 'r')
        tokens = tokenizeText(f.read())
        for token in tokens:
            token = token.lower()
            if token not in wordCounts:
                V +=1
                wordCounts[token] = {}
                if iphone:
                    iphoneWords += 1
                    wordCounts[token]['iphone'] = 1
                    wordCounts[token]['android'] = 0
                else:
                    androidWords += 1
                    wordCounts[token]['android'] = 1
                    wordCounts[token]['iphone'] = 0
            else:
                if iphone:
                    if wordCounts[token]['iphone'] == 0:
                        iphoneWords += 1
                    wordCounts[token]['iphone'] += 1
                else:
                    if wordCounts[token]['android'] == 0:
                        fakeWords += 1
                    wordCounts[token]['android'] += 1
    total = androidCount + iphoneCount
    classProbabilities = {'iphone': iphoneCount/float(total), 'android':androidCount/float(total)}
    return classProbabilities, wordCounts, V, iphoneWords, androidWords


def testNaiveBayes(file, classProbabilities, wordCounts, V, iphoneWords, androidWords, iphoneprobabilities, androidprobabilities, dataset):
    f = open(dataset + '/' + file, 'r')
    tokens = tokenizeText(f.read())
    iphoneNums = []
    androidNums = []
    iphoneNums.append(classProbabilities['iphone'])
    androidNums.append(classProbabilities['android'])
    for token in tokens:
        if token not in wordCounts:
            p = 1 / float(iphoneWords + V)
            iphoneNums.append(p)
            p = 1 / float(androidWords + V)
            androidNums.append(p)
        else:
            # iphone
            p = (wordCounts[token]['iphone'] + 1)/float(iphoneWords + V)
            iphoneNums.append(p)
            iphoneprobabilities[p] = token
            # android
            p = (wordCounts[token]['android'] + 1)/float(androidWords + V)
            androidNums.append(p)
            androidprobabilities[p] = token
    iphoneProb = 1
    androidProb = 1
    for num in iphoneNums:
        iphoneProb *= float(num)
    for num in androidNums:
        androidProb *= float(num)
    if iphoneProb > androidProb:
        return 'iphone'
    else:
        return 'android'
        


def main():
    dataset = sys.argv[1]
    files = os.listdir(dataset)
    N = len(files)
    dataset = dataset.strip('/')
    output = open('naivebayes.output.' + dataset, 'w')
    accurate = 0
    iphoneProbabilities = {}
    androidProbabilities = {}
    for i, file in enumerate(files):
        print(i)
        classProbs, wordCounts, V, iphoneWords, androidWords = trainNaiveBayes(files[:i]+files[i+1:], dataset)
        result = testNaiveBayes(file, classProbs, wordCounts, V, iphoneWords, androidWords, iphoneProbabilities, androidProbabilities, dataset)
        output.write(file + ' ' + result + '\n')
        if 'iphone' in file:
            if result == 'iphone':
                accurate += 1
        else:
            if result == 'android':
                accurate += 1
    output.write('accuracy = '+ str(accurate/float(N)))
    output.close()


if __name__ == "__main__":
    main()