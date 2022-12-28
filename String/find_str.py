'''
find double spaces in string 
'''

st = "this  is a  simple  string."
doubleString = st.find("  ")   # find first double space index 

findRepl = st.replace("  ", " ") # find all double space and replace them with single space
print(doubleString)

print(findRepl)