import requests as r

#id, key
auth = ('b67d3b8c','0e985ceeeb7bcc4f7d5963fe118bf7e7')
#relevant fields
fields = {  'ingredientLines':False,
            'ingredients':False,
            'calories':False,
            'cuisineType':False,
            'mealType':False,
            'dishType':False,
            'totalNutrients':False}

def printFields():
    for i in fields.keys():
        print('{key} - {value}'.format(key=i,value=fields[i]))

def selectField(inputKey):
    #catch + execute
    if inputKey not in fields.keys():
        print('\n"{key}" parameter does not exist\n'.format(key=inputKey))
        return
    elif fields[inputKey]==True:
        print('\n"{key}" parameter already selected\n'.format(key=inputKey))
        return
    else:
        #resets selection
        for i in fields.keys():
            fields.update({i:False})
        #selection
        fields.update({inputKey:True})
        print('\n"{key}" parameter selected\n'.format(key=inputKey))

def requestRecipies(searchKey=None):
    #helper
    def initializeAccessPoint():
        active = None
        #find parameters
        for i in fields.keys():
            if fields[i]==True:
                active = i
        #catch + execute
        if searchKey==None:
            print('\nNo search key\n')
            return
        elif active==None:
            print('\nNo parameters\n')
            return
        else:
            accessPoint = 'https://api.edamam.com/api/recipes/v2?type=public&q={search}&app_id={appId}&app_key={appKey}&field={parameters}'.format(search=searchKey,appId=auth[0],appKey=auth[1],fields=active)
        return accessPoint
    accessPoint = initializeAccessPoint()
    if accessPoint==None:
        return 'n/a'
    else:
        return r.get(accessPoint).text

def requestSavedRecipies():
    return
t = requestRecipies()
print(t)

#f = open('recipedata.txt','w')
#f.write(requestRecipies('chicken'))
#f.close()

