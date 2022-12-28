
letter = ''' Dear <|NAME|>,

Lorem ipsum, or lipsum as it is sometimes known, is dummy text used in laying out print, 
graphic or web designs. The passage is attributed to an unknown typesetter in the 15th century 
who is thought to have scrambled parts of Cicero's De Finibus Bonorum et Malorum for use in a 
type specimen book. It usually begins with: 

You are selected!,
Date: <|DATE|>
'''

name = input("Enter your name ")
date = input("Enter date ")
letter = letter.replace("<|NAME|>", name)
letter = letter.replace("<|DATE|>", date) 

print(letter)