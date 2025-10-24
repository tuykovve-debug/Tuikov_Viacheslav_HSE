import re

def remove_duplicates(text):
    pattern = r'\b(\w+)( \1)+\b'
    while re.search(pattern, text):
        text = re.sub(pattern, r'\1', text)
    return text

some_string = 'раз раз раз раз два три три три три четыре пять пять пять'
result = remove_duplicates(some_string)
print(result)