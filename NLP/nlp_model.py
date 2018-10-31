# -- coding: utf-8 --
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from string import punctuation
import pickle
import jieba


jieba.set_dictionary('dict.txt.big')
add_punc = '，。、【】“”：；（）《》‘’{}？！⑦()、%^>℃：.”“^-——=擅长于的&#@￥」「\n'
all_punc = punctuation+add_punc

def text_process(text):
    nopunc = [char for char in text if char not in all_punc]
    nopunc = ''.join(nopunc)
    return nopunc

train_x = []
train_y = []
train_text = []
origin_corpus = open('train_text.txt', 'r').readlines()

for i in range(len(origin_corpus)):
	current = origin_corpus[i].split(' ')
	text = text_process(current[1])
	text = ' '.join(jieba.cut(text))
	train_x.append(text)
	train_y.append(current[0])

vectorizer = TfidfVectorizer(analyzer='word')
train_x = vectorizer.fit_transform(train_x)

message = '請問國內志工服務有什麼補助嗎？  有嗎有嗎' # input message
target = [' '.join(jieba.cut(text_process(message)))]
test_x = vectorizer.transform(target)

# classification
NB = MultinomialNB().fit(train_x,train_y)
ans = NB.predict(test_x)
# print(ans)

class IntentClassifier:
	def __init__(self):
		self.vectorizer = vectorizer
		self.classifier = NB

	def save_model(self):
		with open('model.pkl', 'wb') as fd:
			model = [self.vectorizer, self.classifier]
			pickle.dump(model, fd)

	def load_model(self):
		with open('model.pkl', 'rb') as fd:
			model = pickle.load(fd)
			self.vectorizer = model[0]
			self.classifier = model[1]

	def predict(self, input):
		target = [' '.join(jieba.cut(text_process(input)))]
		test_x = self.vectorizer.transform(target)
		ans = self.classifier.predict(test_x)
		return ans

classifier = IntentClassifier()
classifier.save_model()
res = classifier.predict(message)
print(res)
