# Language identification

This program was written for educational purposes.
It shows how a language classifier implementing a 3-gram model can be trained on a small data set.
The classifier accepts a string as input and returns the label that corresponds to the detected language.
The data set used to train the classifier must be formatted as csv (comma-separated values): each row of the data set must contain a string with a portion of text and a the corresponding label separated by a comma. For example:

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

The "train.csv" file is provided as a sample data set for training. It contains a list of Spanish, Italian and German cities extracted from the site https://www.simplemaps.com/

The file "es_it_de_fr_pl.json" is an already trained model for detecting Spanish, Italian, German, French and Polish.
