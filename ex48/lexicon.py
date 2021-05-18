lexicon = {
    "north": 'direction',
    "south": 'direction',
    "east": 'direction',
    "go": 'verb',
    "kill": 'verb',
    "eat": 'verb',
    "the": 'stop',
    "in": 'stop',
    "of": 'stop',
    "bear": 'noun',
    "princess": 'noun',
    "1234": 'number',
    "3": 'number',
    "91234": 'number',
    "ASDFADFASDF": 'error',
    "IAS": 'error',

}


def scan(sentence):
    results = []
    words = sentence.split()
    for word in words:
        word_type = lexicon.get(word)
        try:
            results.append((word_type, int(word)))
        except ValueError:
            results.append((word_type, word))
    return results




