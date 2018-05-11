# Gender-Precdictor
Gender predictor is a classifier which detect names gender by analyzing sample text.
Data was downloaded from the [U.S. Social Security](https://www.ssa.gov/oact/babynames/limits.html) website portal for *Beyond the Top 100 Names*. Names included are U.S. nationwide baby names from 2015 with at least five occurences.

To install this package:

```bash
pip install Gender-Predictor
```
#How to use Gender-Predictor?

```python
from gender_predictor.GenderClassifier import classify_gender

print(classify_gender('jitesh'))
```
#Output:
It will give accuracy of gender and gender type 

```python
Accuracy: 0.968143  
F
```

