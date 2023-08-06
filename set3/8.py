def count_words(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        words = content.split()
        return len(words)

def write_word_count(file_path, word_count):
    with open(file_path, 'w') as file:
        file.write(f"Number of words: {word_count}")

input_file = "c:/Users/KULDEEP SINGH NEGI/Desktop/LearningPython/set3/input.txt"
output_file = "c:/Users/KULDEEP SINGH NEGI/Desktop/LearningPython/set3/output.txt"

word_count = count_words(input_file)
write_word_count(output_file, word_count)
