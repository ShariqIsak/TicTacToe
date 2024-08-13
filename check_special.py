import re
import string

def check_spec(string_input):
    regex = re.compile('@_!# $ %^&*()<>?/\|}{~:+-')
    print(any(c in string.punctuation for c in string_input))


choice = 'a'

check_spec(choice)

