from flask import Flask
app=Flask(__name__)
@app.route("/") #End pOint
def hello():
	return "HELLO WORLD2222!!"
def hello1():
	return "I am Varshith!!!"
if __name__=="__main__":
	app.run()