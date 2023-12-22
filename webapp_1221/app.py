from flask import Flask, render_template, url_for, request # url_for 추가

app = Flask(__name__, static_url_path='/static') # ,static_url_path='/static/ 추가

global inputName, inputNum, inputPosition

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/enter/<name>')
def enter(name):
	globals()["inputName"] = name
	return render_template('page.html', name=name)

@app.route('/sideLength', methods=['POST', 'GET'])
def sideLength():
	globals()["inputNum"] = request.args.get('num')
	localNum = int(globals()["inputNum"])
	return render_template('page.html', num=localNum, name=globals()["inputName"])

# DOESN'T WORK YET...
@app.route('/getPosition', methods=['POST', 'GET'])
def getPosition():
	globals()["inputPosition"] = request.args.get('position')
	localPosition = int(globals()["inputPosition"])
	return render_template('page.html', position=localPosition, num=globals()["inputNum"], name=globals()["inputName"])


if __name__=='__main__':
	# threaded=Ture로 넘기면 multiple plot이 가능해집니다.
	app.run(debug=True, threaded=True) #, host="0.0.0.0",port=5000)


# @app.route('/getNumOne')
# def getNumOne():
# 	localNum = int(globals()["inputNum"])
# 	return render_template('page.html', num=localNum, num1=localNum, name=globals()["inputName"])

# @app.route('/getNumTwo')
# def getNumTwo():
# 	localNum = int(globals()["inputNum"])
# 	return render_template('page.html', num=localNum, num2=localNum, name=globals()["inputName"])

# @app.route('/getNumThree', methods=['POST', 'GET'])
# def getNumThree():
# 	localNum = int(globals()["inputNum"])
# 	return render_template('page.html', num=localNum, num3=localNum, name=globals()["inputName"])

# {% if inputNum != "" %}
# <h5><p> The length of the side you entered is {{ num }}.</br>Choose the location of the side below.</p>
# {% else %}
# <h5><p> Please Enter the length of the side </p></h5>
# {% endif %}

                # {% if num=="0" %}
                #     <h5><p> Please Enter the length of the side </p></h5>
                # {% else %}
                #     <h5><p> The length of the side you entered is {{ num }}. </br>
                #     Enter the number of the location of the side.</p></h5>
                # {% endif %}

# {% if num=="0" %}
# <p>NUM = {{ num }}</p>
# {% else %}
# <p>NUM hasn't been set yet</p>
# {% endif %}

