import math
import numpy as np

def main():
	import fasttext

	model = None
	try:
		model = fasttext.load_model('model.bin')
	except Exception:
		model = fasttext.train_unsupervised('sentences.txt', model='skipgram')
		model.save_model('model.bin')

	get_closest_word_to_vector(model['tall'] + model['short'], model)

def get_closest_word_to_vector(vec, model):
	
	closest_word = ""
	distance = math.inf
	for word in model.get_words():
		d = np.linalg.norm(model[word] - vec) 
		if d < distance:
			closest_word = word
			distance = d
			print(distance)
			print(word)
			print("_____")

main()
