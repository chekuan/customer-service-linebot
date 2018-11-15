# 這份檔案是介接 Machine Learning based 的 Intent Identifier 所需要的檔案
# 主要是將 load pretrained model
# 對於 pretrained 好的 model 你可以放在與這個 python 檔案相同的目錄下

import pickle
from string import punctuation

import jieba


jieba.set_dictionary('dict.txt.big')
add_punc = '，。、【】“”：；（）《》‘’{}？！⑦()、%^>℃：.”“^-——=擅长于的&#@￥」「\n'
all_punc = punctuation+add_punc


class IntentClassifier:
	def __init__(self, vectorizer=None, classifier=None):
		self.vectorizer = vectorizer
		self.classifier = classifier

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
		target = [' '.join(jieba.cut(self.text_process(input)))]
		test_x = self.vectorizer.transform(target)
		ans = self.classifier.predict(test_x)
		return int(ans[0])

	def text_process(self, text):
		nopunc = [char for char in text if char not in all_punc]
		nopunc = ''.join(nopunc)
		return nopunc

if __name__ == '__main__':
	# Example
	classifier = IntentClassifier()
	classifier.load_model()
