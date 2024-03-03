# Submission Proyek Data Analisis Dicoding

## Dataset
[Bike Sharing Dataset](https://drive.google.com/file/d/1RaBmV6Q6FYWU4HWZs80Suqd7KQC34diQ/view?usp=sharing) [(Sumber)](https://www.kaggle.com/datasets/lakshmi25npathi/bike-sharing-dataset)

## Folder Structure
```bash
├── Dashboard
│   ├── all_data.csv
│   └── dashboard.py
│   └── bikelogo.jpg
├── Dataset
│   ├── day.csv
│   └── hour.csv
│   └── Readme.txt
├── README.md
├── Proyek_Analisis_Data.ipynb
├── requirements.txt
└── url.txt
```

## Setup environment
```
conda create --name proyek-ds python=3.9
conda activate proyek-ds
pip install numpy pandas scipy matplotlib seaborn jupyter streamlit babel
```

## Run streamlit app (local)
1. Clone this repository
   ```
   [https://github.com/fathanahdz/submission-proyekDA-dicoding.git](https://github.com/fathanahdz/submission-proyekDA-dicoding.git)
   ```
2. Direct the path to the dashboard directory
   ```
   cd Dashboard/dashboard.py
   ```
3. Run streamlit app
   ```
   streamlit run dashboard.py
   ```

## Run streamlit app (cloud)
```
submission-proyekda-dicoding-nfathanahdz.streamlit.app/
```
