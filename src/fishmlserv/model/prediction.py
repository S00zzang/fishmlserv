from sklearn.neighbors import KNeighborsClassifier
import fire
from fishmlserv.model.manager import get_model_path
import pickle

def load_model():
	global fish_model
	if fish_model is None:
		with open(get_model_path(), 'rb') as f:
                	fish_model = pickle.load(f)

	return fish_model


def prediction(l:float, w:float):
	
	m = load_model()

	prediction = m.predict([[l, w]])[0]

	if prediction == 1:
		fish_name = "도미"
	else:
		fish_name = "빙어"

	return fish_name

def main():
	fire.Fire(prediction)
