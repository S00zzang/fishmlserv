from sklearn.neighbors import KNeighborsClassifier
import fire
from fishmlserv.model.manager import get_model_path
import pickle

def prediction(l:float, w:float):
	
	with open(get_model_path(), 'rb') as f:
		fish_model = pickle.load(f)

	prediction = fish_model.predict([[l, w]])[0]

	if prediction == 1:
		fish_name = "도미"
	else:
		fish_name = "빙어"

	return fish_name

def main():
	fire.Fire(prediction)
