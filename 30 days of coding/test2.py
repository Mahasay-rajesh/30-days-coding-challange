'''def convert_to_slug(sentence):
    slug = '-'.join(sentence.replace('?', '').replace('!', '').split())
    return slug
input_sentence = 'Hello World! How are you doing today?'
output_slug = convert_to_slug(input_sentence)
print(output_slug)'''




'''def convert_to_slug(sentence):
    # Remove question marks and exclamation marks, replace spaces with hyphens
    slug = '-'.join(sentence.replace('?', '').replace('!', '').split())
    return slug
# Example usage:
input_sentence = 'Hello World! How are you doing today?'
output_slug = convert_to_slug(input_sentence)
print(output_slug)'''

def convert_to_slug(sentence):
    # Replace question marks and exclamation marks with empty strings
    replaced_sentence = sentence.replace('?', '').replace('!', '')

    # Replace spaces with hyphens
    slug = replaced_sentence.replace(' ', '-')
    
    return slug

# Example usage:
input_sentence = 'Hello World! How are you doing today?'
output_slug = convert_to_slug(input_sentence)
print(output_slug)
