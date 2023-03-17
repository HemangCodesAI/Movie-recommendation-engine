
# Movie Recommendation System

This project is a movie recommendation system that suggests similar movies to the user based on the movie that they select. The dataset used for this project is the TMDb dataset, which contains information about movies, including their titles, overviews, genres, keywords, cast, and crew.

## Dataset

The dataset is divided into two files: tmdb_5000_movies.csv and tmdb_5000_credits.csv. Both files are merged to create a single dataframe movies. The following preprocessing steps are applied to clean the data:

Drop unnecessary columns.
- Remove rows with null values.
- Convert columns containing JSON data into lists of 
- strings.

After preprocessing, the dataset contains the following columns:

- movie_id
- title
- overview
- genres
- keywords
- cast
- crew

## Creating Tags

The tags column is created by merging the genres, keywords, cast, crew, and overview columns into a single column. The following preprocessing steps are applied to clean the tags:

- Remove spaces in the tags.
- Convert tags to lowercase.
- Apply stemming to the tags using the Porter stemmer algorithm.
## Building the Recommendation Engine

The recommendation system uses the cosine similarity measure to find the most similar movies to the selected movie. The steps to build the recommendation system are as follows:

- Convert the tags column into a matrix of token counts using the CountVectorizer function.
- Apply the cosine_similarity function to the matrix to calculate the similarity scores between all pairs of movies.
- Create a function recommend that takes a movie title as input and returns a list of 5 most similar movies along with their posters.

## User Interface

The user interface for the movie recommendation system is built using Streamlit. It consists of a dropdown menu to select the movie and a button to search for similar movies. When the user clicks the search button, the system calls the recommend function and displays the results in a grid of 5 columns. Each column contains the title and poster of a recommended movie.

## Conclusion
The movie recommendation system is a simple yet powerful tool for users to discover new movies based on their interests. The cosine similarity measure provides an efficient way to find similar movies in a large dataset. With the help of Streamlit, the system is easy to use and provides an intuitive interface for the user.








