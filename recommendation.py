from math import sqrt
import os
from euclidean import euclideanDistance

# A partir de um usuario base
# Pega o valor da similaridade desse usuario com todos os outros
def getSimilarity(evaluationTable, userBase, limit=50):
    similarity = [(euclideanDistance(evaluationTable, userBase, userCompare), userCompare)
                    for userCompare in evaluationTable if userCompare != userBase]

    similarity.sort()
    similarity.reverse()

    return similarity[0:limit]

def getUserRecommendations(evaluationTable, userBase, limit=50):
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

def makeSimilarityTable(evaluationTable):
    similarityTable = {}

    for item in evaluationTable:
        scores = getSimilarity(evaluationTable, item)
        similarityTable[item] = scores

    return similarityTable

def getItemRecommendations(evaluationTable, itensSimilarity, userBase, limit=50):
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

    return rankings[0:limit]

def loadUserBase():
    fileDir = os.path.dirname(os.path.realpath('__file__'))
    path = os.path.join(fileDir, 'model/ml-100k')

    itens = {}
    for line in open(path + '/u.item'):
        (id, title) = line.split('|')[0:2]
        itens[id] = title

    userBase = {}
    for line in open(path + '/u.data'):
        (user, idItem, score, time) = line.split('\t')
        userBase.setdefault(user, {})
        userBase[user][itens[idItem]] = float(score)

    return userBase

def makeItemEvaluationBase(evaluationTable):
    evaluationTableTransposed = {}

    for user in evaluationTable:
        for item in evaluationTable[user]:
            evaluationTableTransposed.setdefault(item, {})
            evaluationTableTransposed[item].setdefault(user, evaluationTable[user][item])

    return evaluationTableTransposed
