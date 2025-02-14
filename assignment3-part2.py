import os
import numpy as np
import librosa
from hmmlearn import hmm
from sklearn.metrics import accuracy_score
from jiwer import wer

# Paths to the train and test folders
train_folder = "train"
test_folder = "test"

# TODO: 1. Implement the `extract_mfcc` function to extract MFCC features from an audio file.
# HINT: Use the `librosa` library to load the audio file and extract 13 MFCC features.
# The function should return the transposed MFCC feature array.
def extract_mfcc(file_path, n_mfcc=13):
    y, sr = ...
    mfcc = ...
    return mfcc.T



# TODO: 2. Create a dictionary called `train_data` and populate it with MFCC features for each digit (0-9) from the training folder.
# HINT: Iterate through all files in the `train_folder`, extract the digit label from each filename (e.g., "5_hamdan_m.wav" -> label = 5),
# extract MFCC features using `extract_mfcc`, and store them in the dictionary.
train_data = {}
for file_name in ...:
    if file_name.endswith(".wav"):
        label = ...  # Extract the digit (0-10) as the label
        mfcc_features = extract_mfcc(os.path.join(train_folder, file_name))
        if label not in train_data:
            train_data[label] = []
        train_data[label].append(mfcc_features)

        
        
# TODO: 3. Train a Gaussian HMM for each digit using the data in `train_data`.
# HINT: Use `hmm.GaussianHMM` from `hmmlearn` with 5 components, diagonal covariance type, and 100 iterations.
# Use `np.vstack` to combine feature arrays for each digit before fitting the model.
models = {}
for label, features_list in train_data.items():
    X = ...
    lengths = ...
    model = hmm.GaussianHMM(..., ..., ...)
    model.fit(X, lengths)
    models[label] = model

    
    
# Evaluate on test data
seen_predictions = []
seen_true_labels = []
unseen_predictions = []
unseen_true_labels = []



# TODO: 4. Write a loop to iterate through the files in `test_folder`.
# Extract the true label and speaker name from each file name, predict the most likely label using the trained HMM models,
# and separate predictions for seen speakers (e.g., "hamdan") and unseen speakers (e.g., "sara", "emilio").
train_data = {}
for file_name in os.listdir(test_folder):
    if file_name.endswith(".wav"):
        label = ...
        speaker = ...
        mfcc_features = extract_mfcc(os.path.join(test_folder, file_name))
        
        # Predict the most likely digit using HMMs
        scores = {digit: model.score(mfcc_features) for digit, model in models.items()}
        predicted_label = max(scores, key=scores.get)

        if speaker in ["sara", "emilio"]:  # Unseen speakers
            unseen_predictions.append(predicted_label)
            unseen_true_labels.append(label)
        else:  # Seen speakers
            seen_predictions.append(predicted_label)
            seen_true_labels.append(label)
      
    
    
# Calculate Word Error Rate (WER)
seen_wer = wer(" ".join(map(str, seen_true_labels)), " ".join(map(str, seen_predictions)))
unseen_wer = wer(" ".join(map(str, unseen_true_labels)), " ".join(map(str, unseen_predictions)))

# Print results
print("Word Error Rate (WER) for Seen Speakers: {:.2f}%".format(seen_wer * 100))
print("Word Error Rate (WER) for Unseen Speakers: {:.2f}%".format(unseen_wer * 100))