c={'The':'Vampire','Diaries':'Elena','Damon':'Stefan','Jermey':'Caroline'}
r={'Vampire':'89%','Damon':'65%','Elena':'75%','Stefan':'100%'}
#merge 2 python dictionaries
cr={**c,**r}
print('new dictionary:',cr)
#remove a particular key from the dictionary
cr.pop('Vampire')
print('dictionary after deletion:',cr)
#map two lists into a dictionary
x={'hi','hola','how','kite'}
y={'World','full','hate','mine'}
z=zip(x,y)
d=dict(z)
print('d:',d)
s={'karthick',34,56,89,'daniel'}
print('set :',s)
print('length of the set:',len(s))
s1={1,67,890,23,143}
s2={23,3,1,45,167,12,6}
s3={29,45,7,90,1}
s4={1,2,3,29,7,00}
print('***Original sets***')
print('s1:',s1)
print('s2:',s2)
print('s3:',s3)
print('s4:',s4)
print('remove the intersection of a 2nd set from the 1st set using difference_update():')
s1.difference_update(s2)
print('s1:',s1)
print('s2:',s2)
print('remove the intersection of a 4th set from the 3rd set using -=operator:')
s4-=s3
print('s3:',s3)
print('s4:',s4)
