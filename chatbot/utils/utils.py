# import jieba
# from .invdx import build_data_structures
# from .bm25 import bm25_score
#
#
# jieba.set_dictionary('dict.txt.big')
#
#
# class QueryProcess:
#     def __init__(self):
#         corpus = dict()
#         corpus_num = 4
#         for k in range(1, corpus_num + 1):
#             path = 'corpus/TX' + str(k) + '.txt'
#             text = open(path, 'r').read()
#             seg_list = jieba.lcut(text, cut_all=False)
#             corpus[str(k)] = seg_list
#
#         self.index, self.dlt = build_data_structures(corpus)
#
#     def get_category(self, query):
#         query_result = dict()
#         for term in query:
#             if term in self.index:
#                 doc_dict = self.index[term] # retrieve index entry
#                 for docid, freq in doc_dict.items(): #for each document and its word frequency
#                     score = bm25_score(n=len(doc_dict), f=freq, qf=1, r=0, N=len(self.dlt),
# 									   dl=self.dlt.get_length(docid), avdl=self.dlt.get_average_length())
#                     if docid in query_result:
#                         query_result[docid] += score
#                     else:
#                         query_result[docid] = score
#
#         return query_result


import jieba
import re
from string import punctuation
from .invdx import build_data_structures
from .bm25 import bm25_score


jieba.set_dictionary('dict.txt.big')

add_punc = '，。、【】“”：；（）《》‘’{}？！⑦()、%^>℃：.”“^-——=擅长于的&#@￥」「\n'
all_punc = punctuation+add_punc

class QueryProcess:
    def __init__(self):
        corpus = dict()
        corpus_num = 4
        for k in range(1, corpus_num + 1):
            path = 'corpus/TX' + str(k) + '.txt'
            text = open(path,'r').read()
            text = re.sub(r'[A-Za-z0-9]|/d+','',text)
            segment = jieba.cut(text, cut_all=False)
            segment = ' '.join(segment)
            segment = segment.split(' ')
            seg_list = []
            for i in segment:
                seg_list.append(i)
                if i in all_punc:
                    seg_list.remove(i)
            corpus[str(k)] = seg_list

        self.index, self.dlt = build_data_structures(corpus)

    def get_category(self, query):
        query_result = dict()
        for term in query:
            if term in self.index:
                doc_dict = self.index[term] # retrieve index entry
                for docid, freq in doc_dict.items(): #for each document and its word frequency
                    score = bm25_score(n=len(doc_dict), f=freq, qf=1, r=0, N=len(self.dlt),
									   dl=self.dlt.get_length(docid), avdl=self.dlt.get_average_length())
                    if docid in query_result:
                        query_result[docid] += score
                    else:
                        query_result[docid] = score

        return query_result




