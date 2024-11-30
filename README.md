# NYC-Rental-Property-RAG-Application
A Flask-based web application that utilizes a Retrieval-Augmented Generation (RAG) pipeline to provide an interactive Q&amp;A interface for exploring rental property data in New York City. This aims to answer user queries based on a dataset of NYC rental properties.

![](https://github.com/Khaledayman9/NYC-Rental-Property-RAG-Application/blob/main/Demo.gif)

# Aim
The aim of this app is to provide an interactive platform that allows users to explore and analyze rental property data from New York City. Using a Retrieval-Augmented Generation (RAG) model, the app enables users to ask natural language questions about the dataset, such as property pricing, location, room types, and occupancy details. The app's goal is to offer an intuitive interface for querying the NYC rental market, providing valuable insights into pricing trends, neighborhood characteristics, and other key factors that influence rental properties in the city. By leveraging state-of-the-art NLP techniques like DistilBERT for data retrieval and GPT-2 for generating human-like answers, the app aims to demonstrate the power of combining information retrieval with natural language generation for real-world data analysis.

# Layout

![1](https://github.com/user-attachments/assets/e1343cbc-c215-481d-9d10-93b76340748f)

![2](https://github.com/user-attachments/assets/bf89a11f-6062-439d-a155-55a51f267553)

![3](https://github.com/user-attachments/assets/48da266c-1bc2-4b28-8da6-399a8e0914ea)

![4](https://github.com/user-attachments/assets/7c211a13-051c-470f-b83b-6f98513aab25)

![5](https://github.com/user-attachments/assets/87ca9cfd-f7cf-47f7-bbd0-b1e3bf8c54b8)
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


# Model
The model combines machine learning techniques for embedding generation, similarity search, and natural language response generation.
## 1. Dataset Preparation:
- Loads a CSV file '*ny_rental_data.csv*' containing New York rental property data.
- Selects and cleans relevant columns (latitude, longitude, neighbourhood, etc.) for further processing.
  
## 2. Embedding Generation:
- Uses **DistilBERT**, a lightweight transformer model, to generate vector embeddings for text data (e.g., neighborhoods).
- Converts the text embeddings into a numerical format for similarity searches.

## 3. Similarity Search with FAISS:
- Facebook AI Similarity Search) is a library developed by Facebook AI that specializes in efficient similarity search and clustering of dense vectors.
- Utilizes FAISS, a library for fast similarity search, to index the embeddings.
- Allows retrieval of the most relevant data points based on a user's query.
- Uses L2 distance for similarity search, formula:
  
  ![L2 Distance](https://github.com/user-attachments/assets/6fe9e48a-b739-4e38-9675-9440c3579d4f)


## 4. Text Generation with GPT-2:
- Uses GPT-2, a generative language model, to create human-like answers.
- Takes a query and relevant context as input and generates a response.

## 5. Key Functions:
- *get_embeddings*: Generates embeddings for a list of texts.
- *get_relevant_context*: Retrieves the most relevant contexts from the dataset based on similarity to the query.
- *generate_response*: Generates a natural language answer using the query and relevant context.
- *limit_response_length*: Ensures the generated response does not exceed a specified length.
- *answer_query*: Combines the above steps to retrieve context and generate a coherent answer.


# Routes
The *app.py* file sets up the web application using Flask. It defines the routes that handle requests and responses.
## 1. `/`
- Type: GET
- Purpose: Serves the main page of the app by rendering index.html.
- When the user accesses the root URL (/), the browser displays the user interface, which is defined in the index.html template.

## 2. `/ask`
- Type: POST
- Purpose: Handles queries from the user and returns the generated answer.
- The front-end sends a JSON object containing the user's query to this route.
- The function extracts the query and passes it to the answer_query function in model.py.
- The generated response is returned as a JSON object, which the front-end displays.

# Additional Configurations:
- **CORS:** Enabled to allow cross-origin requests, which is useful if the app needs to interact with other services or front-ends.
- **GPU Configuration:** Disabled GPU usage to ensure compatibility on systems without CUDA.

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
