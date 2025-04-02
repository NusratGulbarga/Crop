# Crop Recommendation System Using Machine Learning

## 📌 Project Overview
The **Crop Recommendation System** is an ML-powered web application that suggests the best crops to grow based on soil and environmental conditions. It uses **Flask**, **Pandas**, **Scikit-learn**, and **Machine Learning** models trained on agricultural datasets.

## 🛠️ Technologies Used
- **Flask** - Backend web framework for API and web application.
- **Pandas** - Data manipulation and preprocessing.
- **Scikit-learn** - Machine Learning model training and prediction.
- **NumPy** - Mathematical operations and array handling.
- **Matplotlib / Seaborn** - Data visualization.
- **SQLite / MySQL** - Database for storing past recommendations and user data.
- **Bootstrap / HTML / CSS** - Frontend UI design.

## 📂 Project Structure
```
CROP-RECOMMENDATION-SYSTEM/
│── app.py                # Main Flask application
│── model.py              # ML model training and saving script
│── static/               # CSS, JS, images
│── templates/            # HTML templates for UI
│── data/                 # Crop dataset
│── saved_model.pkl       # Trained ML model
│── requirements.txt      # Dependencies
│── README.md             # Project documentation
```

## 📦 Installation & Setup
1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/CROP-RECOMMENDATION-SYSTEM.git
   cd CROP-RECOMMENDATION-SYSTEM
   ```
2. **Create Virtual Environment (Optional but Recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## 🏋️‍♂️ Model Training
```bash
# Prepare Data: Ensure you have a dataset (data/crop_data.csv or similar)

# Train the Model
python model.py

# Check for saved model
echo "Check if saved_model.pkl is generated"
```

## 🚀 Running the Flask App
```bash
python app.py
```
Visit `http://127.0.0.1:5000/` in your browser.

## 🎯 Features
✔️ **User Inputs Soil & Weather Data**  
✔️ **ML Model Recommends Best Crop**  
✔️ **Data Visualization & Insights**  
✔️ **User-Friendly Dashboard**  
✔️ **Customizable Model for Different Regions**  

## 📌 Future Enhancements
🔹 **AI-Based Yield Prediction**  
🔹 **Integration with IoT for Live Data**  
🔹 **Mobile App Version**  

## 🤝 Contributing
Feel free to fork, improve, or raise issues in the repository.  
Pull requests are welcome!

## 📜 License
MIT License © 2025 Nusrat

---
**Developed by:** Nusrat | [GitHub](https://github.com/nusratgulbarga)
