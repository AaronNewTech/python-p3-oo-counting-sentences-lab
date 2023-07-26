import re


class MyString:
    # initialize the value to the empty string which is the default value
    def __init__(self, value=''):
        self.value = value

    # get the value of the object
    def get_value(self):
        return self._value

    # set the value of the object
    def set_value(self, value):
        # Check if the value is a string
        if isinstance(value, str):
            self._value = value
            # print the error message if the value is not a string
        else:
            print("The value must be a string.")

    # Check punctuation types
    def is_sentence(self):
        return self.value.endswith('.')

    def is_question(self):
        return self.value.endswith('?')

    def is_exclamation(self):
        return self.value.endswith('!')

    # Count the number of sentences
    def count_sentences(self):
        # Replace the punctuation marks with a unique character (e.g., '#') to count them
        punctuated_text = self.value.replace('.', '~').replace('!', '~').replace('?', '~')
        # Split the text using the unique character '#' to get the sentences which can be split more easily as they are all the same character
        sentences = punctuated_text.split('~')
        # Remove empty strings from the list
        sentences = [sentence.strip() for sentence in sentences if sentence.strip()]
        return len(sentences)

    value = property(get_value, set_value)


# Example usage:
string = MyString()
string.value = "This is a string! It has three sentences. Right?"

print(string.is_sentence())  # Output: False
print(string.is_question())  # Output: False
print(string.is_exclamation())  # Output: True
print(string.count_sentences())  # Output: 3

# Try setting a non-string value
string.value = 123  # Output: "The value must be a string."
