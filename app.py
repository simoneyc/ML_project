from flask import Flask, render_template, request, jsonify
import numpy as np
import joblib
import warnings
warnings.filterwarnings("ignore", category=UserWarning)

app = Flask(__name__)

# 加載模型
try:
    model = joblib.load('random_forest_model.pkl')  # 確保模型文件存在於同一目錄下
except FileNotFoundError as e:
    print(f"模型文件未找到：{e}")
    exit()

# 定義映射字典
growth_rate_mapping = {
    "High": 0,
    "Medium": 2,
    "Low": 1
}

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    probability = None

    if request.method == 'POST':
        try:
            salary = float(request.form['salary'])
            job_satisfaction = int(request.form['job_satisfaction'])
            work_life_balance = int(request.form['work_life_balance'])
            job_security = int(request.form['job_security'])
            industry_growth = request.form['industry_growth']
            
            industry_growth_numeric = growth_rate_mapping.get(industry_growth, 1)

            input_data = np.array([[salary, job_satisfaction, work_life_balance, job_security, industry_growth_numeric]])

            prediction = model.predict(input_data)
            prediction_proba = model.predict_proba(input_data)[:, 1]

            if prediction[0] == 0:
                result = "不會離職"
                probability = 1 - prediction_proba[0]
            else:
                result = "會離職"
                probability = prediction_proba[0]
            probability = f"{probability:.2f}"
        
        except Exception as e:
            result = f"發生錯誤: {str(e)}"

    return render_template('index.html', result=result, probability=probability)

if __name__ == '__main__':
    app.run(debug=True)
