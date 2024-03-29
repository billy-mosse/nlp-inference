import math
import numpy as np

#Entrena el modelo pero tambien lo testea con dev.txt
def main():
	import fasttext

	model = None
	try:
		model = fasttext.load_model('supervised_model.bin')
		print("El modelo ya está cargado!")
	except ValueError:
		model = fasttext.train_supervised('train.txt')
		model.save_model('supervised_model.bin')

	print(model.test('dev.txt'))

main()
