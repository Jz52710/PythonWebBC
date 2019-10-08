import pickle
data = {'name':'盒子','status':'0'}
with open('a.txt','wb') as f:
    pickle.dump(data,f)