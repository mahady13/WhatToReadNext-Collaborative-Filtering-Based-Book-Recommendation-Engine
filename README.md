# WhatToReadNext - Collaborative Filtering Based Book Recommendation Engine

A simple and interactive **Book Recommendation System** built with **Python** and **Streamlit**. The application recommends books based on users' reading preferences using the **Collaborative Filtering** algorithm and **Cosine Similarity**.

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red?style=for-the-badge&logo=streamlit)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Processing-black?style=for-the-badge&logo=pandas)
![NumPy](https://img.shields.io/badge/NumPy-Scientific%20Computing-blue?style=for-the-badge&logo=numpy)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Machine%20Learning-orange?style=for-the-badge&logo=scikitlearn)

---

##  Overview

**WhatToReadNext** helps users discover new books by analyzing reading patterns from thousands of readers.

Instead of recommending books based on genres or keywords, this project uses **Collaborative Filtering**, meaning books are recommended based on how similar readers have rated them.

The recommendation engine is powered by:

- 📚 Collaborative Filtering
- 📐 Cosine Similarity
- 👥 Book-Crossing Dataset from Kaggle (270,000+ books)

---

##  Features

- Search from thousands of book titles
- Top 5 personalized book recommendations
- Displays
  - Book Cover
  - Book Title
  - Author Name
- Fast recommendations using precomputed similarity matrix
- Clean and responsive Streamlit interface

---

##  Machine Learning Workflow

```
Book Ratings Dataset
        │
        ▼
Data Cleaning & Preprocessing
        │
        ▼
User-Book Pivot Table
        │
        ▼
Cosine Similarity Matrix
        │
        ▼
Find Similar Books
        │
        ▼
Recommend Top 5 Books
```

---

##  Tech Stack

| Category | Technology |
|----------|------------|
| Language | Python |
| Framework | Streamlit |
| Data Processing | Pandas, NumPy |
| Model Storage | Joblib |
| Recommendation Algorithm | Collaborative Filtering |
| Similarity Metric | Cosine Similarity |

---

##  Project Structure

```
WhatToReadNext/
│
├── main.py
├── WhatToReadNext.ipynb
├── Books.csv
├── similarity.pkl
├── pivot_table.pkl
├── preprocessed_list
├── requirements.txt
├── .gitignore
└── README.md
```

---

##  How It Works

1. Load the processed dataset.
2. Load the user-book pivot table.
3. Load the cosine similarity matrix.
4. User selects a book.
5. Find the selected book in the pivot table.
6. Retrieve the most similar books.
7. Display the top 5 recommendations with cover images and author names.

---

##  Installation

Clone the repository

```bash
git clone https://github.com/mahady13/WhatToReadNext-Collaborative-Filtering-Based-Book-Recommendation-Engine.git
```

Move into the project

```bash
cd WhatToReadNext-Collaborative-Filtering-Based-Book-Recommendation-Engine
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

##  Dataset

This project uses the **Book-Crossing Dataset**, containing over **270,000 books** along with user ratings.

Dataset includes:

- Book Titles
- Authors
- ISBNs
- Cover Images
- User Ratings

---

##  Recommendation Algorithm

This project implements **Memory-Based Collaborative Filtering**.

### Steps

- Create a User-Book Rating Matrix
- Convert it into a Pivot Table
- Compute Cosine Similarity
- Find the nearest neighboring books
- Recommend the Top 5 most similar books

---

## Future Improvements

- Hybrid Recommendation System
- User Login System
- Search Bar with Auto-complete
- Book Details Page
- Goodreads API Integration
- Deploy on Streamlit Cloud

---

##  Developer

**Mohiuddin Mahady**

- GitHub: https://github.com/mahady13
- LinkedIn: https://linkedin.com/in/mohiuddin-mahady

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.

It helps others discover the project and motivates further development.

---

## 📜 License

This project is developed for educational and portfolio purposes.