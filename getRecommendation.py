from math import sqrt
from euclidean import euclideanDistance
from model.userDatabase import userRatingTable
#from model.movieDatabase import movieRatingTable
import recommendation

movieRatingTable = recommendation.makeItemEvaluationBase(userRatingTable)
tableSimilarity = recommendation.makeSimilarityTable(movieRatingTable)

userRatingLens = recommendation.loadUserBase()
movieRatingLens = recommendation.makeItemEvaluationBase(userRatingLens)
lensSimilarity = recommendation.makeSimilarityTable(movieRatingLens)

def getRecommendationSmallTable():
    print ("\n*******************************************")
    print ("\n*******Recomendando itens ao Usuario*******")
    print ("\n*******************************************")

    print ("\nPara Leonardo: ", str(recommendation.getItemRecommendations(userRatingTable, tableSimilarity, 'Leonardo')))
    print ("\n###########################################\n")

    print ("\nPara Ana: ", str(recommendation.getItemRecommendations(userRatingTable, tableSimilarity, 'Ana')))
    print ("\n###########################################\n")

    print ("\nPara Claudia: ", str(recommendation.getItemRecommendations(userRatingTable, tableSimilarity, 'Claudia')))
    print ("\n###########################################\n")


def getRecommendationMovieLens():
    print ("\n*******************************************")
    print ("\n*******Recomendando itens ao Usuario*******")
    print ("\n*******************************************")

    print ("\n-> Para 1: \n")
    for (score, name) in recommendation.getItemRecommendations(userRatingLens, lensSimilarity, '1'):
        print ("Predição de Score: ", str(score), "Nome: ",str(name), "\n")
    print ("\n###########################################\n")

    print ("\n-> Para 212: \n")
    for (score, name) in recommendation.getItemRecommendations(userRatingLens, lensSimilarity, '212'):
        print ("Predição de Score: ", str(score), "Nome: ",str(name), "\n")
    print ("\n###########################################\n")

    print ("\n-> Para 196: \n")
    for (score, name) in recommendation.getItemRecommendations(userRatingLens, lensSimilarity, '196'):
        print ("Predição de Score: ", str(score), "Nome: ",str(name), "\n")
    print ("\n###########################################\n")

    print ("\n-> Para 2000: \n")
    for (score, name) in recommendation.getItemRecommendations(userRatingLens, lensSimilarity, '2000'):
        print ("Predição de Score: ", str(score), "Nome: ",str(name), "\n")
    print ("\n###########################################\n")
