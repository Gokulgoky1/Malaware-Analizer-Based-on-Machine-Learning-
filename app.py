from flask import Flask,request, url_for, redirect, render_template
import pickle
import numpy as np

app = Flask(__name__)

model=pickle.load(open('model.pkl','rb'))
@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route('/predict',methods=['POST','GET'])
def predict():
    int_features=[float(x) for x in request.form.values()]
    final=[np.array(int_features)]
    prediction=model.predict(final)
    print(prediction)
    if prediction[0]==1:
        return render_template('index.html',pred='File is malware')
    else:
        return render_template('index.html',pred='File is Benign')

if __name__ == '__main__':
    app.run(debug=True)