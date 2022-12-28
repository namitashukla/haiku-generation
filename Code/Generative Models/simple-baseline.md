The simple baseline uses the NLP library Spacy. Here, it uses the Matcher module of Spacy to learn English words and their corresponding POS tags. We define the structure(5-7-5) and the POS tags of the words we expect in the Haiku. Following this, we run a loop where the model randomly selects a word matching the pattern specified to generate Haiku. The entire model is based on guessing technique and the Haiku generated has no meaning.

Input Format: Dataset.csv file which consists of three lines of Haiku is separate columns. It also consists of the corresponding source of the respective Haikus. 

Output Format: A test.csv file which consists of three lines of Haiku is separate columns. This test.csv file is then fed to the GRUEN model which tests it on its quality, toxicity and structure.
