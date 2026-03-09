# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details
This model uses demographic information to predict if an individual makes above or below $50k. 
It was trained using Scikitlean's RandomForestClassifier with 100 estimators and a random state of 42.

## Intended Use
This model was created for an educational project. 
It should not be used for making any real world decisions.

## Training Data
More information on the dataset used for this model can be found here: https://archive.ics.uci.edu/dataset/20/census+income
The dataset has about 32k rows, 80% of which were used for training. 
The dataset included both categorical features (workclass, education, marital-status, occupation, relationship, race, sex, native-country) and continuous features (age, fnlgt, education-num, capital-gain, capital-loss, hours-per-week). 
The categorical features were encoded using OneHotEncoder. 
The target label (salary) was binarized using LabelBinarizer. 
The continuous features were not scaled.

## Evaluation Data
20% of the same dataset was held for testing. 
This data went through the same preprocessing as the training data using the same OneHotEncoder and LabelBinarizer fitted on the training data to avoid data leakage.

## Metrics
_Please include the metrics used and your model's performance on those metrics._
The model was evaluated using Precision, Recall, and F1 score.
Precision: 0.7419 | Recall: 0.6384 | F1: 0.6863


## Ethical Considerations
This dataset includes categories such as sex and race, which may encode historical social biases. It is possible that model predictions may reinforce these biases.


## Caveats and Recommendations
Model performance varies across different population slices. See slice_output.txt for full breakdown. The training dataset was originally from 1994, and may no longer be reflective of modern populations. This model is not intended for making real world decisions. Hyperparameter tuning may improve model performance.