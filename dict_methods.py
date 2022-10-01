#book={
#    1:"Python Programming",
#    2:"Core Python Programming",
#    3:"Advance Python Programming",
#    5.7:'7pm',
#   'p':'Python'
#}
#print(book[3])
#print(book[10])  #KeyError: 10

#g={1:"",2:"Python",3:7,4:6.5,5:[1,4],6:(4,2),7:{4,5},8:{3:"world"}}
##print(g[1],type(g[1])) #<class 'str'>
##print(g[2],type(g[2])) #Python <class 'str'>
#print(g,type(g)) #<class 'dict'>
#print(g.keys())  #dict_keys([1,2,3,4,5,6,7,8])
#print(g.values()) #dict_values(['','Python',7,6.5,[1,4],(4,2),{4,5},{3: 'world'}])
#print(g.items()) #dict_items([(1, ''),(2,'Python'),(3,7),(4,6.5),(5,[1,4]),(6,(4,2)),(7,{4,5}),(8,{3: 'world'})])

#g={1:"",2:"Python",3:7,4:6.5,5:[1,4],6:(4,2),7:{4,5},8:{3:"world"}}
#g.clear()
#print(g) #{}

#a=[120,122,123,125,128,130]
#print(dict.fromkeys(a,'p')) #{120: 'p', 122: 'p', 123: 'p', 125: 'p', 128: 'p', 130: 'p'}
#print(dict.fromkeys(a,54))  #{120: 54, 122: 54, 123: 54, 125: 54, 128: 54, 130: 54}
#print(dict.fromkeys(a,"a")) #{120: 'a', 122: 'a', 123: 'a', 125: 'a', 128: 'a', 130: 'a'}

#g={1:"",2:"Python",3:7,4:6.5,5:[1,4],6:(4,2),7:{4,5},8:{3:"world"}}
#print(g.get(4)) #6.5
#print(g.get(45)) #None
#print(g[44]) #KeyError:44
#g.pop(2)
#print(g)
#g.popitem()
#print(g)

#g={1:"",2:"Python",3:7,4:6.5,5:[1,4],6:(4,2),7:{4,5},8:{3:"world"}}
#g.update({7: 'Sowmya'}) #{1:"",2:"Python",3:7,4:6.5,5:[1,4],6:(4,2),7:'Sowmya',8:{3:"world"}}
#print(g) 
#g.update({9:'Sowmya123'}) #{1:"",2:"Python",3:7,4:6.5,5:[1,4],6:(4,2),7:'Sowmya',8:{3:"world"},9: 'Sowmya123'}
#print(g)
  
#g={1:"",2:"Python",3:7,4:6.5,5:[1,4],6:(4,2),7:{4,5},8:{3:"world"}}
#g.setdefault(8,'Sowmya')
#print(g)
#g.setdefault(10,'sowmya123')
#print(g)

#print(dir(dict()))