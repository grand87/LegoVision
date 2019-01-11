import json

def main():
	print("hello world")

	# generate models according to content of models.json
	
	models_list_file = open("models.json", "r")
	json.load(models_list_file)
	
	return 0
	
if __name__=="__main__":
	main()