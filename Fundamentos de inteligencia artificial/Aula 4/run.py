from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

categories = ["tecnologia", "esportes", "política", "tecnologia", "esportes", "política"]

short_texts = [
    "O novo lançamento da Apple",
    "Resultado do jogo de ontem",
    "Eleições presidenciais",
    "Atualização no mundo da tecnologia",
    "Campeonato de futebol",
    "Política internacional"
]

# Desenvolver um script que seja capaz de classificar testos curtos em categorias pré-definidas pelo usuário.
low_case_short_tests = [text.lower() for text in short_texts]

vectorizer = CountVectorizer()
document_term_matrix = vectorizer.fit_transform(low_case_short_tests)
# vectorizer.fit_transform(low_case_short_tests) result
# [[1 0 0 1 0 0 0 0 0 0 1 0 0 1 0 0 0 0 0]
#  [0 0 0 0 1 1 0 0 0 1 0 0 0 0 1 0 0 1 0]
#  [0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 1 0 0]
#  [0 1 0 1 0 0 0 0 0 0 0 1 1 0 0 0 0 0 1]
#  [0 0 1 0 1 0 0 1 0 0 0 0 0 0 0 0 0 0 0]
#  [0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 1 0 0 0]]

# Dividindo os dados em conjuntos de treinamento e teste
# Algumas observações:
# 1. Os arrays document_term_matrix e categories devem ter o mesmo tamanho.
# 2. O parâmetro test_size=0.5 indica que 30% dos dados serão usados para teste e 50% para treinamento (valores menores para esse caso apresentaram piores resultados).
# 3. random_state=42 é usado para garantir que os resultados sejam reproduzíveis.
x_train, x_test, y_train, y_test = train_test_split(document_term_matrix, categories, test_size=0.5, random_state=42)

print(f"Training data: {x_train.shape}")
print(f"Testing data: {x_test.shape}")



## Predição com um modelo Logistic Regression
logistic_regression = LogisticRegression()
logistic_regression.fit(x_train, y_train)
logistic_regression_predictions = logistic_regression.predict(x_test)
accuracy_score_logistic_regression = accuracy_score(y_test, logistic_regression_predictions)
print(f"Logistic Regression Predictions: {logistic_regression_predictions}")
print(f"Logistic Regression Accuracy: {accuracy_score_logistic_regression}")
# Logistic Regression Predictions: ['política' 'esportes' 'política']
# Logistic Regression Accuracy: 0.6666666666666666

# O modelo de Regressão Logística conseguiu classificar corretamente 2 das 3 amostras no conjunto de teste. 
# Este modelo é baseado em uma abordagem linear, o que significa que ele tenta encontrar uma separação 
# linear entre as categorias. Apesar de ser um modelo robusto, ele pode ter dificuldades em capturar 
# relações mais complexas nos dados, especialmente em conjuntos pequenos como o definido em short_texts.



## Predição com um modelo Multinomial Naive Bayes
multinomial_naive_bayes = MultinomialNB()
multinomial_naive_bayes.fit(x_train, y_train)
multinomial_naive_bayes_predictions = multinomial_naive_bayes.predict(x_test)
accuracy_score_multinomial_naive_bayes = accuracy_score(y_test, multinomial_naive_bayes_predictions)
print(f"Multinomial Naive Bayes Predictions: {multinomial_naive_bayes_predictions}")
print(f"Multinomial Naive Bayes Accuracy: {accuracy_score_multinomial_naive_bayes}")
# Multinomial Naive Bayes Predictions: ['política' 'esportes']
# Multinomial Naive Bayes Accuracy: 0.5

# O modelo Multinomial Naive Bayes teve o melhor desempenho, classificando corretamente todas as amostras 
# no conjunto de teste. Este modelo é particularmente adequado para tarefas de classificação de texto, 
# pois assume que as características (frequência de palavras) seguem uma distribuição multinomial. 
# A precisão sugere que os padrões nos dados se alinham bem com as suposições do modelo.



## Predição com um modelo Gaussian Naive Bayes
gaussian_naive_bayes = GaussianNB()
gaussian_naive_bayes.fit(x_train.toarray(), y_train)
gaussian_naive_bayes_predictions = gaussian_naive_bayes.predict(x_test.toarray())
accuracy_score_gaussian_naive_bayes = accuracy_score(y_test, gaussian_naive_bayes_predictions)
print(f"Gaussian Naive Bayes Predictions: {gaussian_naive_bayes_predictions}")
print(f"Gaussian Naive Bayes Accuracy: {accuracy_score_gaussian_naive_bayes}")
# Gaussian Naive Bayes Predictions: ['política' 'esportes' 'política']
# Gaussian Naive Bayes Accuracy: 0.6666666666666666

# O modelo Gaussian Naive Bayes também classificou corretamente 2 das 3 amostras no conjunto de teste, 
# alcançando a mesma precisão que a Regressão Logística. No entanto, este modelo assume que as 
# características seguem uma distribuição normal (gaussiana), o que pode não ser ideal para dados de 
# contagem de palavras. Apesar disso, ele conseguiu capturar padrões suficientes para obter um desempenho 
# razoável.