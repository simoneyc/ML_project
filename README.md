# ML_project - Career Change Prediction App

This repository contains a machine learning-powered web application for predicting the likelihood of career change based on various personal and industry factors. The app provides a user-friendly interface for inputting data and receiving real-time predictions.

## Features

- **Web Interface:** A responsive and clean front-end built using HTML, Bootstrap, and Flask templates.
- **Prediction Model:** A Random Forest model predicts the likelihood of a career change with probabilities.
- **Interactive GUI:** A secondary desktop GUI application built using `ttkbootstrap` for local predictions.
- **Real-Time Analysis:** Allows users to input salary, job satisfaction, work-life balance, job security, and industry growth rate to determine the likelihood of leaving their job.

## How It Works

1. **Input Data:** Users provide input through the web form or GUI.
   - Salary (numeric)
   - Job Satisfaction (1-10 scale)
   - Work-Life Balance (1-10 scale)
   - Job Security (1-10 scale)
   - Industry Growth Rate (High, Medium, Low)
2. **Prediction Model:** Inputs are processed by a pre-trained Random Forest model (`random_forest_model.pkl`).
3. **Output:** The app provides a binary prediction ("Will Change" or "Won't Change") along with the probability.

## Files in the Repository

- **`index.html`**  
  The HTML template for the Flask app's front-end. It provides a simple form and displays prediction results.

- **`model_test.py`**  
  A desktop application for local predictions. It uses `ttkbootstrap` for a visually appealing interface.

- **`app.py`**  
  The Flask application backend that handles user input, processes the data, and returns predictions.

## Prerequisites

- Python 3.8+
- Libraries: `flask`, `numpy`, `joblib`, `ttkbootstrap`, `scikit-learn`

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/career-change-prediction.git
   cd career-change-prediction
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Place the pre-trained model file (`random_forest_model.pkl`) in the project directory.

4. Run the Flask app:
   ```bash
   python app.py
   ```

5. Open the app in your browser:
   ```
   http://127.0.0.1:5000
   ```

## Usage

### Web Application
1. Navigate to the provided URL after starting the Flask server.
2. Fill in the required fields and click "Predict."
3. View the prediction results directly on the page.

### Desktop Application
1. Run `model_test.py`:
   ```bash
   python model_test.py
   ```
2. Use the graphical interface to input data and view predictions.

## Screenshots

![Web Interface](screenshot-web.png)  
*Example of the web application interface.*

![Desktop GUI](screenshot-gui.png)  
*Example of the desktop application interface.*

## Contributing

Contributions are welcome! Please fork this repository and submit a pull request for any features or improvements.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
