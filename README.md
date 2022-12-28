# haiku-generation
Generating Haikus using AI
Haikus are known for their ability to paint a vivid picture in just a few words regarding a particular topic. 
They are 3-line long structured poems and they comprise of a fixed syllable scheme (5-7-5).Hence, Haiku generation is an example of a strictly constrained task. In addition, Haikus stand out amongst other poetry forms due to theirflexibility in terms of topic, rhyme, and concise syntax.
We have implemented various models published in the literature and their extensions to be able to generate good Haikus. These model implementations include SpaCy, novel CharRNN using LSTM, CharRNN using LSTM + Syllable structure
and exploring variants of GPT (like GPTJ). Since, the task involves the generation of text legible to humans, the performance of the models is being evaluated by the quality of Haikus generated. For this, we are using GRUEN as the quality metric and average syllable count per line to evaluate the structure of haiku. The best results were obtained using Fine-tuned GPT-J with the max GRUEN score of 0.544 and the mean syllable structure of [4.9, 7.05, 5.10].
