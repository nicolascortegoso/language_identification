from classifier import Classifier

c = Classifier()

# Trains a model from a dataset
c.train('train.csv')

# Identifies the language from a string
print(c.predict("Este es un ejemplo de español"))
print(c.predict("Questo è un esempio di italiano"))
print(c.predict("Dies ist ein Beispiel für Deutsch"))

# Saves the trained model to a json file
c.save_model("trained_model.json")

#Loads a trained model
c.load_model("es_it_de_fr_pl.json")

print(c.predict("Ceci est un exemple de français"))
print(c.predict("To jest przykład języka polskiego"))
