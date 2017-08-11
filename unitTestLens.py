from math import sqrt
from euclidean import euclideanDistance


import recomendation

userRatingTable = recomendation.loadBase()
movieRatingTable = recomendation.loadBase()
################################################################################

def testUserSimilarity():
    print ("\n****Similaridade Entre Usuarios:\n")
    print ("\nAna: \n", str(recomendation.getSimilarity(userRatingTable, '1')))

def testUserEuclidean():
    print ("\n****Distância Euclidiana entre 2 usuarios:\n")
    print ("1 e 212: ", str(euclideanDistance(userRatingTable, '1','212')))

def testUserRecomendation():
    print ("\n****Recomendando para um usuario:\n")
    print ("\nRecomendações para 1: ", str(recomendation.getUserRecommendations(userRatingTable, '1')))

    print ("\nRecomendações para 212: ", str(recomendation.getUserRecommendations(userRatingTable, '212')))


def userTestAll():
    testUserSimilarity()
    testUserEuclidean()
    testUserRecomendation()

################################################################################

def testMovieSimilarity():
    print ("\n****Similaridade entre 1 Filme e os outros:\n")
    print ("\nStar Wars: \n", str(recomendation.getSimilarity(movieRatingTable, '50')))

def testMovieEuclidean():
    print ("\n****Distância Euclidiana entre 2 Filmes:\n")
    print ("Star Trek e Star Wars: ", str(euclideanDistance(movieRatingTable, '222','50')))

def testMovieRecomendation():
    print ("\n****Recomendando para um Filme:\n")
    print ("\nRecomendações para Star Trek: ", str(recomendation.getUserRecommendations(movieRatingTable, '222')))

    print ("\nRecomendações para Star Wars: ", str(recomendation.getUserRecommendations(movieRatingTable, '50')))

def movieTestAll():
    testMovieSimilarity()
    testMovieEuclidean()
    testMovieRecomendation()
