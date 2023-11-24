import re

def create_files(file_name):
    LARGE_WORDS = "files/large-words.txt"
    SMALL_WORDS = "files/small-words.txt"
    INPUT_FILE = file_name
    words = set()
    with open(SMALL_WORDS,"w") as small_words:
        with open(LARGE_WORDS,"w") as large_words:
            with open(INPUT_FILE,"r") as input_file:
                for line in input_file:
                    for word in line.split():
                        words.add(word)
                        if(len(word)<3):
                            small_words.write(word+"\n")
                        else:
                            large_words.writelines(word+"\n")
    return len(words)



def ex3():
    total_words = create_files("files/words.txt")
    print(f"Total words: {total_words}.")

ex3()