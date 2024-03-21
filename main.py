import EdamamAPI as eda

edamamData = eda.getRecipeData('chicken',1)

for i in edamamData.items():
    print('{item}\n'.format(item=i))