# NYC-Rental-Property-RAG-Application
A Flask-based web application that utilizes a Retrieval-Augmented Generation (RAG) pipeline to provide an interactive Q&amp;A interface for exploring rental property data in New York City. This aims to answer user queries based on a dataset of NYC rental properties.

# Aim
The aim of this app is to provide an interactive platform that allows users to explore and analyze rental property data from New York City. Using a Retrieval-Augmented Generation (RAG) model, the app enables users to ask natural language questions about the dataset, such as property pricing, location, room types, and occupancy details. The app's goal is to offer an intuitive interface for querying the NYC rental market, providing valuable insights into pricing trends, neighborhood characteristics, and other key factors that influence rental properties in the city. By leveraging state-of-the-art NLP techniques like DistilBERT for data retrieval and GPT-2 for generating human-like answers, the app aims to demonstrate the power of combining information retrieval with natural language generation for real-world data analysis.

# Features
- Interactive query interface using a web app.
- Retrieves and answers questions based on rental property data.
- Real-time response generation with dynamic animations.
- Contextual query handling using a custom RAG pipeline.


# Dataset
- The app uses a lightweight dataset[^1] of NYC rental properties that contains key information such as:
  - **Location:** Latitude and Longitude
  - **Neighborhood:** Area names in New York City
  - **Room Types:** Types of rooms available for rent
  - **Pricing:** Rental prices
  - **Occupancy Measures**: Days occupied, number of reviews, minimum nights required
- This dataset is ideal for beginners looking to practice their data analytics and machine learning skills.

- Key Features:
  - **Query Interface:** Users can ask questions about NYC rental properties, including price, location, room types, and reviews.
  - **RAG Model:** The app combines retrieval-based and generation-based methods, retrieving relevant data from the dataset, and then using a language model to generate coherent, contextually accurate answers.
  - **Data Insights:** The app allows users to gain insights into the NYC rental market, exploring the relationships between pricing, location, and occupancy.
  - **User Experience:** Interactive UI with word-by-word answer display, a loading spinner, and real-time answers.
**Powered by DistilBERT for text embedding and GPT-2 for generating responses, the app offers a smooth and responsive querying experience.**
[^1]: [NY Rental Properties Pricing](https://www.kaggle.com/datasets/ivanchvez/ny-rental-properties-pricing)

# Installation
## 1. Clone the repository:
```bash
git clone https://github.com/<your-username>/my-rental-app.git](https://github.com/Khaledayman9/NYC-Rental-Property-RAG-Application.git)
```
## 2. Navigate to the project directory:
```bash
cd NYC-Rental-Property-RAG
```

## 3. Create and activate a virtual environment:
### On Linux:
```bash
python -m venv myenv
source myenv/bin/activate 
```
### On Windows:
```bash
python -m venv myenv
myenv\Scripts\activate
```


## 4. Install dependencies:
```bash
pip install -r requirements.txt
```

## 5. Run the app:
```bash
python app.py
```



# Usage:
**- Open a web browser and navigate to http://127.0.0.1:5000/.**

**- Ask questions related to NYC rental properties in the input field.**

# Technologies
- **Backend**: Flask
- **Frontend**: HTML, CSS, JavaScript
- **Machine Learning**: Transformers, FAISS for similarity search
- **Database**: CSV file
