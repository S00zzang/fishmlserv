def get_model_path():
	my_path = __file__
	#home/s00zzang/code/fishmlserv/src/fishmlserv/model/manager.py
	dir_name = os.path.dirname(my_path)
	#home/s00zzang/code/fishmlserv/src/fishmlserv/model
	model_path = os.path.join(dir_name , "model.pkl")
	#home/s00zzang/code/fishmlserv/src/fishmlserv/model/model.pkl

	return model_path
	
	
	
