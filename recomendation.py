from math import sqrt
import os
from euclidean import euclideanDistance

# A partir de um usuario base
# Pega o valor da similaridade desse usuario com todos os outros
def getSimilarity(evaluationTable, userBase, limit=30):
    similarity = [(euclideanDistance(evaluationTable, userBase, userCompare), userCompare)
                    for userCompare in evaluationTable if userCompare != userBase]

    similarity.sort()
    similarity.reverse()

    return similarity[0:limit]

def getUserRecommendations(evaluationTable, userBase, limit=30):
    totais = {}
    similaritySum = {}

    for userCompare in evaluationTable:
        if userCompare == userBase: continue

        similarity = euclideanDistance(evaluationTable, userBase, userCompare)

        if similarity <= 0: continue

        for item in evaluationTable[userCompare]:
            if item not in evaluationTable[userBase]:
                totais.setdefault(item, 0)
                totais[item] += evaluationTable[userCompare][item] * similarity
                similaritySum.setdefault(item, 0)
                similaritySum[item] += similarity

    rankings = [(total/similaritySum[item], item) for item, total in totais.items()]
    rankings.sort()
    rankings.reverse()

    return rankings[0:limit]

def loadBase():
    fileDir = os.path.dirname(os.path.realpath('__file__'))
    path = os.path.join(fileDir, 'model/ml-100k')

    movies = {}
    for line in open(path + '/u.item'):
        (id, title) = line.split('|')[0:2]
        movies[id] = title

    userBase = {}
    for line in open(path + '/u.data'):
        (user, idMovie, score, time) = line.split('\t')
        userBase.setdefault(user, {})
        userBase[user][movies[idMovie]] = float(score)

    return userBase

def makeSimilarityTable(evaluationTable):
    similarityTable = {}

    for item in evaluationTable:
        scores = getSimilarity(evaluationTable, item)
        similarityTable[item] = scores

    return similarityTable

def getItemRecommendations(evaluationTable, itensSimilarity, userBase):
    userItens = evaluationTable[userBase]
    scores = {}
    totalSimilarity = {}

    for (item, score) in userItens.items():
        for(similarity, unassistedItem) in itensSimilarity[item]:
            if unassistedItem in userItens: continue

            scores.setdefault(unassistedItem, 0)
            scores[unassistedItem] += similarity * score
            totalSimilarity.setdefault(unassistedItem, 0)
            totalSimilarity[unassistedItem] += similarity

    rankings = [(score/totalSimilarity[item], item) for item, score in scores.items()]
    rankings.sort()
    rankings.reverse()

    return rankings
