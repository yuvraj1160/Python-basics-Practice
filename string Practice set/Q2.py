'''Q2 -> Write a program to fill in a letter template given below with name and date. '''

# Code 

letter = '''
Dear <|Name|>,
You are selected!
<|Date|>
'''
print(letter.replace("<|Name|>", "Harry").replace("<|Date|>", "15 May 2030"))