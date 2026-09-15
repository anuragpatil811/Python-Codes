v = '''Virat Kohli[a] (born 5 November 1988) is an Indian international cricketer and the former all-format captain of the Indian national cricket team.[3] He is a right-handed batter and occasional right-arm medium pace bowler. Considered one of the greatest all-format batsmen in the history of cricket, he has been nicknamed the King, the Chase Master, and the Run Machine for his skills, records and ability to lead his team to victory.[4] Kohli has the most centuries in ODIs and the second-most centuries in international cricket with 85 tons across all formats. He is also the leading run-scorer in the Indian Premier League.[5] Kohli is the most successful Test captain of India with most wins and 3 consecutive Test mace retainments.[6] 
He is the only batter to earn 900+ rating points across all 3 formats.[7]'''

#**Count**
#print(v.count('Indian'))

#**Upper()**
#print(v.upper())
#print(v.lower())
#print(v.title())
#print(v.capitalize())

#Find the number of words in the string usingabove methods only
#print(v.count(' ')+1)

#Display Virat Kohli
#print(v[0:5].join([' ', 'Kohli']))
q = [12, 23, 34, 45, 56, 57, 7]
#print(q[1:4:-1])
#print(q[ : -10: 2])
#print(q[: -6  :2])

#Example:
p =  'this is data science and we are learning python python is a programming language'
#capitalize  first character of each word
#print(p.title())
#find the count of unique words in the string
print(len(set(p.split())))
