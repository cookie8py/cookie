from flask import Flask, render_template, url_for, request # url_for 추가

app = Flask(__name__, static_url_path='/static') # ,static_url_path='/static/ 추가

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/enter/<name>')
def enter(name):
	return render_template('page.html', name=name)

# 여기부터 추가한 부분
# GET 방식으로 값을 전달 받습니다.
# num이라는 이름을 가진 integer variable을 넘겨받습니다.
# 아무 값도 넘겨받지 않는 경우도 있으므로 비어 있는 url도 함께 mapping해줘야 합니다. 
@app.route('/calculate', methods=['POST', 'GET'])
def calculate(num=None):
	# 어떤 http metod를 이용해서 전달받았는지를 아는 것이 필요합니다.
	# 아래에서 보는 바와 같이 어떤 방식으로 넘어왔느냐에 따라서 읽는 방식이 달라집니다.
	if request.method == 'POST':
		# temp = request.form['num']
		pass
		
	elif request.method == 'GET':
		## 넘겨받은 숫자
		temp = request.args.get('num')
		temp = int(temp)
		## 넘겨받은 문자
		# temp1 = request.args.get('char1')
		## 넘겨받은 값을 원래 페이지로 리다이렉트
		return render_template('page.html', num1=temp) # , char1=temp1)
	## else 로 하지 않은 것은 POST, GET 이외에 다른 method로 넘어왔을 때를 구분하기 위함

	elif request.method == 'GET':
		## 넘겨받은 숫자
		temp = request.args.get('num')
		temp = int(temp)
		## 넘겨받은 문자
		# temp1 = request.args.get('char1')
		## 넘겨받은 값을 원래 페이지로 리다이렉트
		return render_template('page.html', num2=temp) # , char1=temp1)
	## else 로 하지 않은 것은 POST, GET 이외에 다른 method로 넘어왔을 때를 구분하기 위함

	elif request.method == 'GET':
		## 넘겨받은 숫자
		temp = request.args.get('num')
		temp = int(temp)
		## 넘겨받은 문자
		# temp1 = request.args.get('char1')
		## 넘겨받은 값을 원래 페이지로 리다이렉트
		return render_template('page.html', num3=temp) # , char1=temp1)
	## else 로 하지 않은 것은 POST, GET 이외에 다른 method로 넘어왔을 때를 구분하기 위함

if __name__=='__main__':
	# threaded=Ture로 넘기면 multiple plot이 가능해집니다.
	app.run(debug=True, threaded=True) #, host="0.0.0.0",port=5000)