import requests as r

#id, key
auth = ('b67d3b8c','0e985ceeeb7bcc4f7d5963fe118bf7e7')
search = ''
fields = {'uri':False,
                  'label':False,
                  'image':False,
                  'images':False,
                  'source':False,
                  'url':False,
                  'shareAs':False,
                  'yield':False,
                  'dietLabels':False,
                  'healthLabels':False,
                  'cautions':False,
                  'ingredientLines':False,
                  'ingredients':False,
                  'calories':False,
                  'gylcemicIndex':False,
                  'inflammatoryIndex':False,
                  'totalCO2Emissions':False,
                  'co2EmissionsClass':False,
                  'totalWeight':False,
                  'totalTime':False,
                  'cuisineType':False,
                  'mealType':False,
                  'dishType':False,
                  'totalNutrients':False,
                  'totalDaily':False,
                  'digest':False,
                  'tags':False,
                  'externalId':False}
def nextLine():
    print('\n')

def printFields():
    parameters = fields.keys()
    for i in parameters:
        print('{key} - {value}'.format(key=i,value=fields[i]))
    nextLine()

def toggleFields(inputKey):
    if inputKey not in fields:
        print('{key} parameter does not exist'.format(inputKey))
        return
    if fields[inputKey] == False:
        fields.update({inputKey:True})
    else:
        fields.update({inputKey:False})
    print('"{key}" parameter set to {value}'.format(key=inputKey,value=fields[inputKey]))
    nextLine()

printFields()
toggleFields('shareAs')
printFields()