def getUserA(user_electricity, originalElectricity_list):
    tempList = []
    for electricity in originalElectricity_list:
        tempList.append(electricity.UserA)
    user_electricity['UserA'] = tempList
    return user_electricity


def getUserB(user_electricity, originalElectricity_list):
    tempList = []
    for electricity in originalElectricity_list:
        tempList.append(electricity.UserB)
    user_electricity['UserB'] = tempList
    return user_electricity


def getUserC(user_electricity, originalElectricity_list):
    tempList = []
    for electricity in originalElectricity_list:
        tempList.append(electricity.UserC)
    user_electricity['UserC'] = tempList
    return user_electricity


def getUserD(user_electricity, originalElectricity_list):
    tempList = []
    for electricity in originalElectricity_list:
        tempList.append(electricity.UserD)
    user_electricity['UserD'] = tempList
    return user_electricity


def getUserF(user_electricity, originalElectricity_list):
    tempList = []
    for electricity in originalElectricity_list:
        tempList.append(electricity.UserF)
    user_electricity['UserF'] = tempList
    return user_electricity


def getUserG(user_electricity, originalElectricity_list):
    tempList = []
    for electricity in originalElectricity_list:
        tempList.append(electricity.UserG)
    user_electricity['UserG'] = tempList
    return user_electricity


def getUserH(user_electricity, originalElectricity_list):
    tempList = []
    for electricity in originalElectricity_list:
        tempList.append(electricity.UserH)
    user_electricity['UserH'] = tempList
    return user_electricity


def getUserI(user_electricity, originalElectricity_list):
    tempList = []
    for electricity in originalElectricity_list:
        tempList.append(electricity.UserI)
    user_electricity['UserI'] = tempList
    return user_electricity


def getUserJ(user_electricity, originalElectricity_list):
    tempList = []
    for electricity in originalElectricity_list:
        tempList.append(electricity.UserJ)
    user_electricity['UserJ'] = tempList
    return user_electricity


def getUserK(user_electricity, originalElectricity_list):
    tempList = []
    for electricity in originalElectricity_list:
        tempList.append(electricity.UserK)
    user_electricity['UserK'] = tempList
    return user_electricity


def getUserL(user_electricity, originalElectricity_list):
    tempList = []
    for electricity in originalElectricity_list:
        tempList.append(electricity.UserL)
    user_electricity['UserL'] = tempList
    return user_electricity


def getUserM(user_electricity, originalElectricity_list):
    tempList = []
    for electricity in originalElectricity_list:
        tempList.append(electricity.UserM)
    user_electricity['UserM'] = tempList
    return user_electricity


def getUserN(user_electricity, originalElectricity_list):
    tempList = []
    for electricity in originalElectricity_list:
        tempList.append(electricity.UserN)
    user_electricity['UserN'] = tempList
    return user_electricity


def getUserO(user_electricity, originalElectricity_list):
    tempList = []
    for electricity in originalElectricity_list:
        tempList.append(electricity.UserO)
    user_electricity['UserO'] = tempList
    return user_electricity


def getUserP(user_electricity, originalElectricity_list):
    tempList = []
    for electricity in originalElectricity_list:
        tempList.append(electricity.UserP)
    user_electricity['UserP'] = tempList
    return user_electricity


def getUserQ(user_electricity, originalElectricity_list):
    tempList = []
    for electricity in originalElectricity_list:
        tempList.append(electricity.UserQ)
    user_electricity['UserQ'] = tempList
    return user_electricity


def getUserR(user_electricity, originalElectricity_list):
    tempList = []
    for electricity in originalElectricity_list:
        tempList.append(electricity.UserR)
    user_electricity['UserR'] = tempList
    return user_electricity


def getUserS(user_electricity, originalElectricity_list):
    tempList = []
    for electricity in originalElectricity_list:
        tempList.append(electricity.UserS)
    user_electricity['UserS'] = tempList
    return user_electricity


def getUserT(user_electricity, originalElectricity_list):
    tempList = []
    for electricity in originalElectricity_list:
        tempList.append(electricity.UserT)
    user_electricity['UserT'] = tempList
    return user_electricity


userDict = {
    'UserA': getUserA,
    'UserB': getUserB,
    'UserC': getUserC,
    'UserD': getUserD,
    'UserF': getUserF,
    'UserG': getUserG,
    'UserH': getUserH,
    'UserI': getUserI,
    'UserJ': getUserJ,
    'UserK': getUserK,
    'UserL': getUserL,
    'UserM': getUserM,
    'UserN': getUserN,
    'UserO': getUserO,
    'UserP': getUserP,
    'UserQ': getUserQ,
    'UserR': getUserR,
    'UserS': getUserS,
    'UserT': getUserT
}


def getEveryUserElectricity(user_electricity, originalElectricity_list,user):
    #user_electricity = userDict.get(user)(user_electricity, originalElectricity_list)
    #return user_electricity
    return userDict.get(user)(user_electricity, originalElectricity_list)
