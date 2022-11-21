from gensim.models import word2vec, Word2Vec
import pprint
model = Word2Vec.load('model2016')
pprint.pprint(model.wv.most_similar(positive = ['political','protest','demonstration'],restrict_vocab=15000, topn = 20))
#pprint.pprint(model.predict_output_word(['protest','political'], topn=20))