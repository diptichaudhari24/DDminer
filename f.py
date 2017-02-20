
from flask import Flask, render_template, request, jsonify
app = Flask(__name__)
import scheduling


@app.route('/')
def index():
    # Render template
    return render_template('index.html')


@app.route('/post', methods=['POST'])
def post():
    # Get the parsed contents of the form data
    post_data = request.json
    age = post_data[u'inputData'][u'age']
    sex = post_data[u'inputData'][u'sex']
    result = scheduling.predict(age,sex)
    print "main result :" + result[0]
    post_data[u'inputData'][u'prediction'] = result[0]
    post_data[u'inputData'][u'grid1'] = result[1]
    post_data[u'inputData'][u'grid2'] = result[2]
    post_data[u'inputData'][u'grid3'] = result[3]
    print post_data[u'inputData'][u'prediction']
    return jsonify(post_data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=90)

