import re

#Regex Fubnction
#1]findall() : Returns a list containing all matches
txt="Its a pleasant day to work todayday"
get_match=re.findall("day",txt)
print(get_match)
#o/p : ['day', 'day','day']

#2]search() : returns a Match object if there is a match.
email = "john.doe@example.com hsdihk yes.dbh"
pattern = r"@(.+)$"
result = re.search(pattern, email)
print(result)
print(result.span())
print(result.start())
print(result.end())
print(result.group())

"""
group() returns the substring that was matched by the 
RE. start() and end() return the starting and ending index of the match. 
span() returns both start and end indexes in a single tuple.
o/p : <re.Match object; span=(8, 35), match='@example.com hsdihk yes.dbh'>
        (8,35)
        8
        35
        @example.com hsdihk yes.dbh"""

#3]sub():Replaces one or many matches with a string
txt="Hi!!Im Tejal Rahate?##$@43 , How you doing ?345@!"
pattern="[0-9#$@]"
clean_txt=re.sub(pattern,"",txt)

"""
1]. - any character
2]^ - starts with
3]$ - ends with
4]* - 0 or more occurance
5]+ - 1 or more occurance
6]? - 0 or more occurance
7]{}- specified no of occurance
8]| - Either 
9]()- capture a group 
10]\d	Returns a match where the string contains digits (numbers from 0-9)
11]\D	Returns a match where the string DOES NOT contain digits
12]\s	Returns a match where the string contains a white space character
13]\S	Returns a match where the string DOES NOT contain a white space character
14]\w	Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)
15]\W	Returns a match where the string DOES NOT contain any word characters
16][0-5][0-9]	Returns a match for any two-digit numbers from 00 and 59

"""