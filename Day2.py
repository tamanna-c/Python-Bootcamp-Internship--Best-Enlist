Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print("30 days 30 hours challenge")
30 days 30 hours challenge
>>> hours = "thirty"
>>> print("hours")
hours
>>> print(hours)
thirty
>>> days = "thirty days"
>>> print(days[0])
t
>>> print(days[0:5])
thirt
>>> challenge="I will win"
>>> print(challenge[2:10])
will win
>>> print(challenge[7:10])
win
>>> print(len(challenge))
10
>>> challenge="I will win"
>>> print(challenge.lower())
i will win
>>> print(challenge.upper())
I WILL WIN
>>> a="30 days"
>>> b="30 hours"
>>> c=a+b
>>> print(c)
30 days30 hours
>>> print(a+ " "+b)
30 days 30 hours
>>> test = "thirty days and thirty hours"
>>> x = test.casefold()
>>> print(x)
thirty days and thirty hours
>>> x = test.capitalize()
>>> print(x)
Thirty days and thirty hours
>>>  x = test.find(x)
 
SyntaxError: unexpected indent
>>> x = test.find(x)
>>> print(x)
-1
>>> x  = test.isalpha()
>>> print(x)
False
>>> x = test.isalnum()
>>> print(x)
False
>>> 