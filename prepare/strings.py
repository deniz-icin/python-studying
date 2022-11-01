"""Functions for creating, transforming, and adding prefixes to strings."""
def add_prefix_un(word):
    prefix = "un"
    return prefix + word
    
def make_word_groups(vocab_words):
    prefix_word = []
    prefix = vocab_words[0]
    for _ in vocab_words:
        if _ != prefix:
            final_words = prefix + _
            prefix_word.append(final_words)
    prefix_word.insert(0, prefix)
    return ' :: '.join(prefix_word)

def remove_suffix_ness(word):
    if word[-4:] == "ness":
        new_word = word[:-4]
    if new_word[-1] == "i":
        new_word = new_word[:-1] + "y"
    return new_word

def adjective_to_verb(sentence, index):
    new_word = sentence.split()[index]
    return new_word.rsplit('.', 1)[0] + "en"
