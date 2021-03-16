import gensim
from gensim import models
from gensim.models import Word2Vec
from sklearn.metrics.pairwise import cosine_similarity
from commands import main_commands
import numpy as np
from model_download import downloadModel

downloadModel()

print("Loading NLP model...")
model = gensim.models.KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300.bin.gz', binary=True, limit=500000)
print("Finished loading NLP model.")

word_replacements = {
    'unmute': 'my mic on',
    'mute': 'my mic off',
    'start': 'turn on',
    'stop': 'turn off',
    'audio': 'mic',
    'microphone': 'mic',
    'camera': 'video',
    'call': 'meeting',
    'view': 'open',
    'check': 'open',
    'exit': 'close',
    'open': 'turn on',
    'close': 'turn off'

}

def cleanStr(str):
    for word, repl in word_replacements.items():
        str = str.replace(word, repl)
    return str

def forceVectorize(word):
    vec = np.zeros((300,))
    for i, char in enumerate(word):
        vec[i] = (ord(char)/256 - 0.5)
    return vec
    

def vectorize(str):
    str = cleanStr(str)
    return sum([model[word] if word in model.vocab else forceVectorize(word) for word in str.split()]).reshape(1, -1)

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
