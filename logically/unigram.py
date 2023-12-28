from itertools import chain

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score
from tqdm import tqdm


import torch
import spacy
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim

# initialize hyper hyper parameters
torch.manual_seed(420)
np.random.seed(420)

# load data
fallacies_df = pd.read_csv('./data/fallacies.csv', index_col=0)
approved_df = pd.read_csv('./data/approved.csv', index_col=0)

df = pd.concat([
    fallacies_df,
    approved_df[approved_df.n_supporters >= 5].drop("n_supporters", axis=1)
])
df.fallacy_reason = df.fallacy_reason.fillna('')
df = df[~df.premise_content.isna()]

vc = df.fallacy_type.value_counts()

df = df[df.fallacy_type.isin(vc.head(10).index)]

# text preprocessing
nlp = spacy.load('en_core_web_sm')
def preprocess_sentence(sent):
    sent = sent.lower()
    sent = nlp(sent)
    words = map(lambda x: x.text, sent)
    return list(words)
df['premise_content_preprocessed'] = df.premise_content.apply(preprocess_sentence)
df = df.sample(frac=1, random_state=420).reset_index(drop=True) # shuffle the data
train_df, test_df = train_test_split(df, test_size=0.1, random_state=420)
word_vocab = {"<oov>", "<pad>"}
word_vocab = word_vocab.union(
    set(chain.from_iterable(map(lambda x: x[1]["premise_content_preprocessed"], train_df.iterrows())))
)
word_to_ix = {word: i for i, word in enumerate(word_vocab)}
fallacy_vocab = sorted(list(set(df.fallacy_type.unique())))
fallacy_to_ix = {word: i for i, word in enumerate(fallacy_vocab)}

# Neural Net
class Net(nn.Module):
    def __init__(self, word_vocab_size, word_embedding_dim, fallacy_vocab_size, max_sent_size):
        super(Net, self).__init__()

        self.word_embeddings = nn.Embedding(
            word_vocab_size, word_embedding_dim
        )  # random init

        hidden = 100
        self.fc1 = nn.Linear(word_embedding_dim, hidden)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(hidden * max_sent_size, fallacy_vocab_size)

    def forward(self, word_inputs):
        word_embeds = self.word_embeddings(word_inputs)
        h1 = self.fc1(word_embeds)
        a1 = self.relu(h1)
        h2 = self.fc2(a1.view(a1.shape[0], -1))
        return h2

MAX_SENT_SIZE = 100
def pad_and_convert_to_ints(data):
    X = np.full((len(data), MAX_SENT_SIZE), word_to_ix["<pad>"])

    for i, (_, x) in enumerate(data.iterrows()):
        X[i, :len(x["premise_content_preprocessed"])] = [
            (word_to_ix[word] if word in word_to_ix else word_to_ix['<oov>'])
            for word in x["premise_content_preprocessed"]
        ]

    return X

trainX = pad_and_convert_to_ints(train_df)
testX = pad_and_convert_to_ints(test_df)
trainY = train_df.fallacy_type.apply(lambda x: fallacy_to_ix[x]).values
testY = test_df.fallacy_type.apply(lambda x: fallacy_to_ix[x]).values

net = Net(
    len(word_vocab),
    300,
    len(fallacy_vocab),
    MAX_SENT_SIZE,
)
opt = optim.Adam(net.parameters(), lr=0.001, betas=(0.9, 0.999))
criterion = nn.CrossEntropyLoss()


def train_epoch(X, Y, model, opt, criterion, batch_size=50):
    model.train()
    losses = []
    for beg_i in range(0, X.shape[0], batch_size):
        x_batch = X[beg_i: beg_i + batch_size, :]
        y_batch = Y[beg_i: beg_i + batch_size]
        x_batch = torch.tensor(x_batch)
        y_batch = torch.tensor(y_batch)

        opt.zero_grad()

        y_pred = model(x_batch)

        loss = criterion(y_pred, y_batch)

        loss.backward()

        opt.step()

        losses.append(loss.data.numpy())

    return [sum(losses) / float(len(losses))]

e_losses = []
num_epochs = 50
for e in tqdm(range(num_epochs)):
    e_losses += train_epoch(trainX, trainY, net, opt, criterion, batch_size=100)
e_losses