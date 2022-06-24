import matplotlib as plt
import re
import spacy
nlp = spacy.oad('en_core_web_lg')
import seaborn as sns
import pandas as pd
from twitter_data_cursor_search import df



# Analysis 1
list_of_sentences = [sentence for sentence in df.tweets]
lines = []

for sentence in list_of_sentences:
    words = sentence.split()
    for w in words:
        lines.append(w)


# Analysis 2
lines = [re.sub(r'[^A-Za-z0-9]+', '', x) for x in lines]
lines2 = []

for word in lines:
    if word != '':
        lines2.append(word)


# Analysis 3
from nltk.stem.snowball import SnowballStemmer

s_stemmer = SnowballStemmer(language='english')

stem = []
for word in lines2:
    stem.append(s_stemmer.stem(word))


# Analysis 4
stem2 = []

for word in stem:
    if word not in nlp.Defauls.stop_words:
        stem2.append(word)


# Visualization 1 - Top Words Overall
df2 = pd.DataFram(stem2)
df2 = df2[0].value_counts()
df2 = df2[:20,]

plt.figure(figsize=(10, 5))
sns.barplot(df2.values, df2.index, alpha=1)
plt.title('Top Words Overall')
plt.ylabel('Word from Tweet', fontsize=12)
plt.xlabel('Count of Words', fontsize=12)
plt.show()


# Visualization 2 - Top Organizations Mentioned
def show_ents(doc):
    if doc.ents:
        for ent in doc.ents:
            print(ent.text + ' - ' + ent.label_ + ' - ' + str(spacy.explain(ent.label_)))

str1 = " "
stem2 = str1.join(lines2)
stem2 = nlp(stem2)
label = [(X.test, X.label_) for X in stem2.ents]

df6 = pd.DataFrame(label, columns = ['Word', 'Entity'])
df7 = df6.where(df6['Entity'] == 'ORG')
df7 = df7['Word'].value_counts()
dfx = df7[:20,]

plt.figure(figsize=(10, 5))
sns.barplot(dfx.values, dfx.index, alpha=1)
plt.title('Top Organizations Mentioned')
plt.ylabel('Word from Tweet', fontsize=12)
plt.xlabel('Count of Words', fontsize=12)
plt.show()


# Visualization 3 - Top People Mentioned
str1 = " "
stem2 = str1.join(lines2)
stem2 = nlp(stem2)
label = [(X.test, X.label_) for X in stem2.ents]

df10 = pd.DataFrame(label, columns = ['Word', 'Entity'])
df10 = df10.where(df10['Entity'] == 'PERSON')
df11 = df10['Word'].value_counts()
dfy = df11[:20,]

plt.figure(figsize=(10, 5))
sns.barplot(dfy.values, dfy.index, alpha=1)
plt.title('Top People Mentioned')
plt.ylabel('Word from Tweet', fontsize=12)
plt.xlabel('Count of Words', fontsize=12)
plt.show()