import  pandas as pd


data1 = pd.DataFrame({
    "Name":["Zairul","Mazwan","Jilani", "Tom", "Alicia", "Beckham"],
    "Group":["Red","Red","Blue", "Blue", "Red","Red"]
})

data2 = pd.DataFrame({
    "Course":["CS","CS","SE", "CS", "CS", "SE"],
    "Level":["4","5","4", "5","4", "5"]
})


dataset = pd.concat([data1, data2], axis=1)
print(dataset)
numpyDset = dataset.values

print("Numpy dataset : ",numpyDset)
print("Numpy dataset slice : ",numpyDset[:,1])

