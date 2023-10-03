def to_array(text):
    if text =='':
        return []
    return text.split(', ')

print(to_array(''))