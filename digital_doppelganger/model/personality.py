import nltk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation

def analyze_personality(text_data):
    nltk.download('stopwords')
    from nltk.corpus import stopwords

    # Text preprocessing
    stop_words = set(stopwords.words('english'))
    text_data = [' '.join([word for word in text.split() if word.lower() not in stop_words]) for text in text_data]

    # Vectorization
    vectorizer = CountVectorizer(max_features=1000)
    text_vector = vectorizer.fit_transform(text_data)

    # Latent Dirichlet Allocation for personality profiling
    lda = LatentDirichletAllocation(n_components=5, random_state=42)
    lda.fit(text_vector)

    # Map traits to topics
    traits = ['Openness', 'Conscientiousness', 'Extraversion', 'Agreeableness', 'Neuroticism']
    return {trait: lda.components_[i].sum() for i, trait in enumerate(traits)}
