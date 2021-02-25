import gensim
from gensim import models
from gensim.models import Word2Vec
from sklearn.metrics.pairwise import cosine_similarity
from commands import main_commands

model = gensim.models.KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300.bin.gz', binary=True, limit=500000)

word_replacements = {
    'unmute': 'my mic on',
    'mute': 'my mic off',
    'start': 'turn on',
    'stop': 'turn off',
    'audio': 'mic',
    'microphone': 'mic',
    'camera': 'video',

}

def cleanStr(str):
    for word, repl in word_replacements.items():
        str = str.replace(word, repl)
    return str

def vectorize(str):
    str = cleanStr(str)
    return sum([model[word] for word in str.split() if word in model.vocab]).reshape(1, -1)

def mostSimilar(str, lstOfStr):
    mostSim = None
    bestScore = 0

    vectorizedStr = vectorize(str)
    
    for aStr in lstOfStr:
        score = cosine_similarity(vectorizedStr, vectorize(aStr))
        if score > bestScore:
            bestScore = score[0][0]
            mostSim = aStr
    print((mostSim, bestScore))
    return (mostSim, bestScore) if bestScore > .5 else (str, 0)


vectorized_commands = {key: vectorize(key) for key, val in main_commands.items()}
