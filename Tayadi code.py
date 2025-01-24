
import pandas as pd
import numpy as np

animals = pd.DataFrame({
    'col1': ['A', 'A', 'B', np.nan, 'D', 'C'],
    'col2': [2, 1, 9, 8, 7, 4],
    'weight': [0, 1, 9, 4, 2, 3],
    'name': ['a', 'B', 'c', 'D', 'e', 'F']
})

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    df = animals[animals.weight>2]
    print(df)
    df.sort_values('weight',ascending=False,inplace=True)
    df1=pd.DataFrame(df['name'])
    print(df['name'])
    return df1



findHeavyAnimals(animals)




import sys
sys.exit(0)

# randomly select choices in dropdown
import itertools

vehical = ["honda1","honda2",["honda3","BMW","oddy"],["toyota","toyotaLE","scorpio"],"Hundai"]
week = ["mon","tue","wed","thur","fri"]

new_list = []
final_car_list = []

def nwlogic(i):
    for j in i:
        if j not in new_list:
            return j

for i in range(3):
    for i in vehical:
        if type(i)== list:
            i = nwlogic(i)
        new_list.append(i)
    final_car_list.append(new_list)

list2 = sum(final_car_list, [])
print(list2)



day_list = []
i = 0
for days in itertools.cycle(week):
    day_list.append(days)
    i+=1
    if i >= len(list2):
        break
print(day_list)

resulted_list = list(zip(list2,day_list))
print(resulted_list)

