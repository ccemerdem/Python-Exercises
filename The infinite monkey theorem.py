import random
import string


def generateString(stringLength):
    sampleList = list(string.ascii_lowercase)
    sampleList.append(" ")
    return "".join(random.choices(sampleList, k=stringLength))


def scoreString(randomString):
    score = 0
    example = list("methinks it is like a weasel")
    list(randomString)

    for n in range(0, 28):
        if randomString[n] == example[n]:
            score += 100 / 28
    return score


def callFunctions(stringLength, iterationCount):
    bestScore = 0
    bestMatching = "none"
    for i in range(iterationCount):
        randomString = generateString(stringLength)
        score = scoreString(randomString)
        if score > bestScore:
            bestScore = score
            bestMatching = randomString

    print("Score: %.2f / 100" % (bestScore))
    print("Best Matching: %s" % (bestMatching))


# stringLength (must >= 28), iterationCount
callFunctions(28, 10000)
