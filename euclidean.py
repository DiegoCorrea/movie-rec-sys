from math import sqrt

# Distância Euclidiana
# raizDa(soma-De-1-Ate-N((usuarioBase - usuarioComparacao)aoQuadrado))
def euclideanDistance(evaluationTable, userBase, userCompare):
    si = {}

    for item in evaluationTable[userBase]:
        if item in evaluationTable[userCompare]: si[item] = 1

    if len(si) == 0: return 0

    distance = sum([pow(evaluationTable[userBase][item] - evaluationTable[userCompare][item], 2)
                for item in evaluationTable[userBase] if item in evaluationTable[userCompare]])

    return 1/(1 + sqrt(distance))
