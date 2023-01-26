"""
Textwrap
The textwrap module provides two convenient functions: wrap() and fill().
"""

import textwrap
string = "This is a very very very very very long string."
#The wrap() function wraps a single paragraph in text (a string) so that every line is width characters long at most.
# return list of string of given width
print (textwrap.wrap(string,4))
# ['This', 'is a', 'very', 'very', 'very', 'very', 'very', 'long', 'stri', 'ng.']


#The fill() function wraps a single paragraph (a string)in text and returns a single string containing the wrapped paragraph.
# fill(string, width) => return string of given width
print (textwrap.fill(string,4))
"""
This
is a
very
very
very
very
very
long
stri
ng.
"""