from flask import Flask, render_template, request
import pickle
import pandas as pd


app = Flask(__name__)
model = pickle.load(open("xgboostv4.pkl", 'rb'))



@app.route('/')  # To render Homepage
def home_page():
    return render_template('index.html')


@app.route('/result', methods=['POST'])  # This will be called from UI
def prediction():
    if request.method == 'POST':
        age = int(request.form['age'])
        education_num = int(request.form['edu_num'])
        capital_gain = int(request.form['cap_gain'])
        capital_loss = int(request.form['cap_loss'])
        hours_per_week = int(request.form['hrs_work'])
        sex = int(request.form['gender'])
        workclass = int(request.form['work_class'])
        education = int(request.form['edu'])
        marital_status = int(request.form['marital_status'])
        occupation = int(request.form['Occ'])
        relationship = int(request.form['relation'])
        race = int(request.form['race'])
        native_country = int(request.form['country'])

        parameter = [age, education_num, capital_gain, capital_loss, hours_per_week, workclass, education, marital_status, occupation, relationship, race, sex,
                     native_country]


        result = model.predict([parameter])

        if result == 1:
            ans = 'Salary > 50K'
        else:
            ans = 'Salary < 50K'

        return render_template('index.html', result=ans)


if __name__ == '__main__':
    app.run(debug=True)
