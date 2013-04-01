Viterbi-algorithm
=================

The Viterbi algorithm is tagging algorithm based on TRIGRAM HIDDEN MARKOV MODELS (TRIGRAM HMMS)
To improve upon the Viterbi algorithm,i.e. to handle rare and unseen words I have created 4 new classes of words 'RARE','ALLCAPS','NUMERIC' and 'LASTCAP'
in addition to the already present 'O' and 'I-GENE'.Words appearing less than 5 times are classified depending on 'ALLCAPS','NUMERIC' and 'LASTCAP'.If a word appears
less than 5 times and does not belong to any of the previous mentioned 3 classes then it is classified as 'RARE'.
This creation of different word classes hepls to improve the Viterbi algorithm.
