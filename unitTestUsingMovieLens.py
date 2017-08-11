from math import sqrt

from euclidean import euclideanDistance
import recommendation

userRatingTable = recommendation.loadBase()
movieRatingTable = recommendation.loadBase()

tableSimilarity = recommendation.makeSimilarityTable(movieRatingTable)
################################################################################

def testUserSimilarity():
    print ("\n*******************************************")
    print ("\n********Similaridade Entre Usuarios********")
    print ("\n*******************************************")
    print ("\nAna: \n", str(recommendation.getSimilarity(userRatingTable, '1')))
    print ("\n###########################################\n")

def testUserEuclidean():
    print ("\n*******************************************")
    print ("\n***Distância Euclidiana entre 2 usuarios***")
    print ("\n*******************************************")
    print ("1 e 212: ", str(euclideanDistance(userRatingTable, '1','212')))
    print ("\n###########################################\n")

def testUserrecommendation():
    print ("\n*******************************************")
    print ("\n********Recomendando para 1 usuario********")
    print ("\n*******************************************\n")
    print ("\nRecomendações para 1: ", str(recommendation.getUserRecommendations(userRatingTable, '1')))
    print ("\n###########################################\n")
    print ("\nRecomendações para 212: ", str(recommendation.getUserRecommendations(userRatingTable, '212')))
    print ("\n###########################################\n")


def userTestAll():
    testUserSimilarity()
    testUserEuclidean()
    testUserrecommendation()

################################################################################

def testMovieSimilarity():
    print ("\n****Similaridade entre 1 Filme e os outros:\n")
    print ("\nStar Wars: \n", str(recommendation.getSimilarity(movieRatingTable, '50')))

def testMovieEuclidean():
    print ("\n****Distância Euclidiana entre 2 Filmes:\n")
    print ("Star Trek e Star Wars: ", str(euclideanDistance(movieRatingTable, '222','50')))

def testMovierecommendation():
    print ("\n****Recomendando para um Filme:\n")
    print ("\nRecomendações para Star Trek: ", str(recommendation.getUserRecommendations(movieRatingTable, '222')))

    print ("\nRecomendações para Star Wars: ", str(recommendation.getUserRecommendations(movieRatingTable, '50')))

def movieTestAll():
    testMovieSimilarity()
    testMovieEuclidean()
    testMovierecommendation()


def testItemBased():
    recommendation.getItemRecommendations(userRatingTable, tableSimilarity, 'Leonardo')
