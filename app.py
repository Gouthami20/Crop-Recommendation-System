#agricentral,kisansuvidha
from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
app = Flask(__name__,template_folder='templates')
with open('crop.pkl','rb') as f:
        model=pickle.load(f)

#standard_to = MinMaxScaler()
@app.route("/", methods=['GET','POST'])
def main():
        #Fuel_Type_Diesel=0
        if request.method == 'POST':
                nitrogen=request.form.get("a")
                phosphorus=request.form.get("b")
                potassium=request.form.get("c")
                temperature=request.form.get("d")
                humidity=request.form.get("e")
                ph=request.form.get("f")
                rainfall=request.form.get("g")
                crop=['rice', 'maize', 'kidney beans', 'black gram', 'pomegranate','banana','mango', 'grapes', 'apple', 'orange', 'papaya','coconut', 'cotton', 'jute', 'coffee']
                a=np.array([[nitrogen, phosphorus, potassium, temperature, humidity, ph, rainfall]])
                x=a.astype(np.float)
                prediction=model.predict(x)
                prediction=model.predict([[nitrogen, phosphorus, potassium, temperature, humidity, ph, rainfall]])

                print(prediction)
                #output=round(prediction[0],2)
                #rec_crop=crop[prediction]
                if prediction == 'rice':
                        return render_template('main.html', result='The recommended crop is RICE')
                if prediction == 'maize':
                        return render_template('main.html', result='The recommended crop is MAIZE')
                if prediction == 'kidney beans':
                        return render_template('main.html', result='The recommended crop KIDNEY BEANS')
                if prediction == 'black gram':
                        return render_template('main.html', result='The recommended crop is BLACK GRAM')
                if prediction == 'pomegranate':
                        return render_template('main.html', result='The recommended crop is POMEGRANATE')
                if prediction == 'banana':
                        return render_template('main.html', result='The recommended crop is BANANA')
                if prediction == 'mango':
                        return render_template('main.html', result='The recommended crop is MANGO')
                if prediction == 'grapes':
                        return render_template('main.html', result='The recommended crop is GRAPES')
                if prediction == 'apple':
                        return render_template('main.html', result='The recommended crop is APPLE')
                if prediction == 'orange':
                        return render_template('main.html', result='The recommended crop is ORANGE')
                if prediction == 'mouth beans':
                        return render_template('main.html', result='The recommended crop is Moth Beans')
                if prediction == 'mung bean':
                        return render_template('main.html', result='The recommended crop is Mung Bean')
                if prediction == 'peas':
                        return render_template('main.html', result='The recommended crop is Peas')
                if prediction == 'papaya':
                        return render_template('main.html', result='The recommended crop is PAPAYA')
                if prediction == 'coconut':
                        return render_template('main.html', result='The recommended crop is COCONUT')
                if prediction == 'cotton':
                        return render_template('main.html', result='The recommended crop is COTTON')
                if prediction == 'jute':
                        return render_template('main.html', result='The recommended crop is JUTE')
                if prediction == 'coffee':
                        return render_template('main.html', result='The recommended crop is COFFEE')
        else:
                return render_template('main.html')
if __name__=="__main__":
        app.run(debug=True)