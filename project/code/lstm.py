from google.colab import drive
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelBinarizer
from keras.preprocessing import text, sequence
from keras.preprocessing.text import Tokenizer
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense,LSTM, Flatten
from keras.layers.embeddings import Embedding

drive.mount('/content/drive')

df = pd.read_csv('/content/drive/MyDrive/599/pdb_data_no_dups.csv').merge(pd.read_csv('/content/drive/MyDrive/599/pdb_data_seq.csv'), how='inner', on='structureId')
# Drop rows with missing labels
df = df[[type(c) == type('') for c in df.classification.values]]
df = df[[type(c) == type('') for c in df.sequence.values]]
# select proteins
df = df[df.macromoleculeType_x == 'Protein']
df.reset_index()

# count numbers of instances per class
cnt = Counter(df.classification)
top_classes = 10
# sort classes
sorted_classes = cnt.most_common()[:top_classes]
classes = [c[0] for c in sorted_classes]
counts = [c[1] for c in sorted_classes]
df = df[[c in classes for c in df.classification]]

# Transform labels to one-hot
lb = LabelBinarizer()
Y = lb.fit_transform(df.classification)

max_length = 256

#create and fit tokenizer
tokenizer = Tokenizer(char_level=True)
tokenizer.fit_on_texts(seqs)
#represent input data as word rank number sequences
X = tokenizer.texts_to_sequences(seqs)
X = sequence.pad_sequences(X, maxlen=max_length)

embedding_dim = 8

#  model
model = Sequential()
model.add(Embedding(len(tokenizer.word_index)+1, embedding_dim, input_length=max_length))
model.add(LSTM(128,return_sequences=True))
model.add(LSTM(128))
model.add(Dense(top_classes, activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
print(model.summary())

#  train
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=.2)
model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=50, batch_size=256)
