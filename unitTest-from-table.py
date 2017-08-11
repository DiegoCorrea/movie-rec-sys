from math import sqrt
from euclidean import euclideanDistance
from model.userDatabase import userRatingTable
from model.movieDatabase import movieRatingTable

import recomendation

################################################################################

def testUserSimilarity():
    print ("\n****Similaridade Entre Usuarios:\n")
    print ("\nAna: \n", str(recomendation.getSimilarity(userRatingTable, 'Ana')))

def testUserEuclidean():
    print ("\n****Distância Euclidiana entre 2 usuarios:\n")
    print ("Ana e Marcos: ", str(euclideanDistance(userRatingTable, 'Ana','Marcos')))

def testUserRecomendation():
    print ("\n****Recomendando para um usuario:\n")
    print ("\nRecomendações para Leonardo: ", str(recomendation.getUserRecommendations(userRatingTable, 'Leonardo')))

    print ("\nRecomendações para Ana: ", str(recomendation.getUserRecommendations(userRatingTable, 'Ana')))

    print ("\nRecomendações para Marcos: ", str(recomendation.getUserRecommendations(userRatingTable, 'Marcos')))

    print ("\nRecomendações para Pedro: ", str(recomendation.getUserRecommendations(userRatingTable, 'Pedro')))

    print ("\nRecomendações para Janaina: ", str(recomendation.getUserRecommendations(userRatingTable, 'Janaina')))


def userTestAll():
    testUserSimilarity()
    testUserEuclidean()
    testUserRecomendation()

################################################################################

def testMovieSimilarity():
    print ("\n****Similaridade entre 1 Filme e os outros:\n")
    print ("\nStar Wars: \n", str(recomendation.getSimilarity(movieRatingTable, 'Star Wars')))

def testMovieEuclidean():
    print ("\n****Distância Euclidiana entre 2 Filmes:\n")
    print ("Star Trek e Star Wars: ", str(euclideanDistance(movieRatingTable, 'Star Trek','Star Wars')))

def testMovieRecomendation():
    print ("\n****Recomendando para um Filme:\n")
    print ("\nRecomendações para Star Trek: ", str(recomendation.getMovieRecommendations(movieRatingTable, 'Star Trek')))

    print ("\nRecomendações para Star Wars: ", str(recomendation.getMovieRecommendations(movieRatingTable, 'Star Wars')))

    print ("\nRecomendações para Exterminador do Futuro: ", str(recomendation.getMovieRecommendations(movieRatingTable, 'Exterminador do Futuro')))

    print ("\nRecomendações para Norbit: ", str(recomendation.getMovieRecommendations(movieRatingTable, 'Norbit')))

    print ("\nRecomendações para Freddy x Jason: ", str(recomendation.getMovieRecommendations(movieRatingTable, 'Freddy x Jason')))

def movieTestAll():
    testMovieSimilarity()
    testMovieEuclidean()
    testMovieRecomendation()
