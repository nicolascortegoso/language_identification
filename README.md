# Language identification

This program was written for educational purposes.
It shows how a language classifier implementing a 3-gram model can be trained on a small data set.
The classifier accepts a string as input and returns a tuple. The first element of the tuple indicates the label of the detected language, while the second element contains a dictionary that includes the values of all the label. The chosen label corresponds to the one with the highest value.

For example:

```  
('ES', {'ES': -222.61510574574257, 'IT': -254.0790300358609, 'DE': -239.07137895266186})
```
"ES" is selected over "IT" and "DE" because it has a higher value.

## Training the model

The data set used to train the classifier is required to be formatted as a csv file (comma-separated values): each row of the data set must contain a string with a portion of text and a the corresponding label separated by a comma. For example:

```  
Madrid,ES
Barcelona,ES
Sevilla,ES
Málaga,ES
Boscoreale,IT
Spinea,IT
Mogliano Veneto,IT
Parabiago,IT
Sant’Anastasia,IT
Leinfelden-Echterdingen,DE
Neumarkt,DE
Hückelhoven,DE
Hofheim,DE
```

The *"train.csv"* file is provided as a sample data set for training. It contains a list of Spanish, Italian and German cities extracted from the site https://www.simplemaps.com/

## Saving and loading a trained model

The trained classifier generates a model. This model can be saved to a JSON file so that next time the classifier can be used directly without training.

The file *"es_it_de_fr_pl.json"* is an already trained model for detecting Spanish, Italian, German, French and Polish.
