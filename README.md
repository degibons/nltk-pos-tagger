# NLTK POS Tagger service

Shipped with treebank_NaiveBayes_aubt trained tagger (accuracy: 0.98178).

[Penn Treebank POS tags](https://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html )


# Docker usage

` docker build -t nltk-pos-tagger .  `

` docker run -d -p 8888:80 nltk-pos-tagger `

**Send POST** request to ` localhost:8888 ` with english text to tag (param ` text `):

 `'text': 'The Volga is the longest river in Europe.'`

**Recieve JSON** response with tagged text (param `tagged_text`):

`{ "tagged_text": [
        [
            "The",
            "DT"
        ],
        [
            "Volga",
            "NNP"
        ],
        [
            "is",
            "BEZ"
        ],
        [
            "the",
            "DT"
        ],
        [
            "longest",
            "JJS"
        ],
        [
            "river",
            "NN"
        ],
        [
            "in",
            "IN"
        ],
        [
            "Europe",
            "NNP"
        ],
        [
            ".",
            "."
        ]
    ]
} `
