#Andrew Liang
#251308760
import requests as r

#id, key
auth = ('b67d3b8c','0e985ceeeb7bcc4f7d5963fe118bf7e7') #incase of api limit

#intializes the access point
def __initializeAccessPoint(searchKey=None):
    #catch + execute
    if searchKey==None:
        print('\nNo search key\n')
        return None
    else:
        accessPoint = 'https://api.edamam.com/api/recipes/v2?type=public&q={search}&app_id={appId}&app_key={appKey}&field=url'.format(search=searchKey,appId=auth[0],appKey=auth[1])
    return accessPoint

#requests the recipe links
def __requestRecipeLinks(searchKey=None):
    accessPoint = __initializeAccessPoint(searchKey)
    if accessPoint==None:
        req = 'n/a'
    else:
        req = r.get(accessPoint).text
    return req


def __refineRecipeLinks(rawData):
    removedStrings = ['"','{','}','hits:[recipe:url:','_links:self:href:','recipe:url:',',title:Self']
    rawData = rawData[:-21]
    for i in removedStrings:
        rawData = rawData.replace(i,'')
    rawList = [x for x in rawData.split(',') if 'edamam' in x and 'href' not in x]      
    return rawList

def __requestRawRecipeData(recipesList,limit):
    rawRecipeData = {}
    count = 0
    for i in recipesList:
        if count!=limit:
            req = r.get(i).text
            count+=1
        else:
            break
        req = req.replace('"','')
        ingredientString = req[req.find('ingredients:')+12:req.find(',calories')]
        name = req[req.find('label:')+6:req.find(',image')]
        ingredientString = ingredientString.split('},{')
        ingredientList = [x.split(',') for x in ingredientString]
        rawRecipeData[name] = ingredientList
    return rawRecipeData

def __refineRecipeData(recipesList):
    for i in recipesList:
        ingredientList = []
        for j in recipesList[i]:
            ingredientValues = [x for x in j if 'quantity:' in x or 'measure:' in x or 'food:' in x]
            ingredientList.append(ingredientValues)
        recipesList[i] = ingredientList
    return recipesList

def getRecipeData(searchKey, limit=1):
    recipeLinks = __requestRecipeLinks(searchKey)
    recipeLinks = __refineRecipeLinks(recipeLinks)
    if recipeLinks!='n/a':    
        recipeData = __requestRawRecipeData(recipeLinks,limit)
        recipeData = __refineRecipeData(recipeData)
        return recipeData
    else:
        return None