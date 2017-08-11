from math import sqrt
from euclidean import euclideanDistance
from model.userDatabase import userRatingTable
from model.movieDatabase import movieRatingTable

import recommendation

################################################################################

def testUserEuclidean():
    print ("\n*******************************************")
    print ("\n***Distância Euclidiana entre 2 usuarios***")
    print ("\n*******************************************")
    print ("Ana e Marcos: ", str(euclideanDistance(userRatingTable, 'Ana','Marcos')))
    print ("\n###########################################\n")

def testUserSimilarity():
    print ("\n*******************************************")
    print ("\n********Similaridade Entre Usuarios********")
    print ("\n*******************************************")
    print ("\nAna: \n", str(recommendation.getSimilarity(userRatingTable, 'Ana')))
    print ("\n###########################################\n")

def testUserrecommendation():
    print ("\n*******************************************")
    print ("\n********Recomendando para 1 usuario********")
    print ("\n*******************************************")
    print ("\nPara Leonardo: ", str(recommendation.getUserRecommendations(userRatingTable, 'Leonardo')))
    print ("\n###########################################\n")

    print ("\nPara Ana: ", str(recommendation.getUserRecommendations(userRatingTable, 'Ana')))
    print ("\n###########################################\n")

    print ("\nPara Marcos: ", str(recommendation.getUserRecommendations(userRatingTable, 'Marcos')))
    print ("\n###########################################\n")

    print ("\nPara Pedro: ", str(recommendation.getUserRecommendations(userRatingTable, 'Pedro')))
    print ("\n###########################################\n")

    print ("\nPara Janaina: ", str(recommendation.getUserRecommendations(userRatingTable, 'Janaina')))
    print ("\n###########################################\n")

def userTestAll():
    testUserEuclidean()
    testUserSimilarity()
    testUserrecommendation()

################################################################################

def testItemSimilarity():
    print ("\n*******************************************")
    print ("\n****Similaridade entre 1 Filme e a base****")
    print ("\n*******************************************\n")
    print ("\nStar Wars: \n", str(recommendation.getSimilarity(movieRatingTable, 'Star Wars')))
    print ("\n###########################################\n")

def testItemEuclidean():
    print ("\n*******************************************")
    print ("\n****Distância Euclidiana entre 2 Filmes****")
    print ("\n*******************************************\n")
    print ("Star Trek e Star Wars: ", str(euclideanDistance(movieRatingTable, 'Star Trek','Star Wars')))
    print ("\n###########################################\n")

def itemTestAll():
    testItemSimilarity()
    testItemEuclidean()
