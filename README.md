# Content Based Filtering Model

<h1>Recommendation though review of the tourism places</h1>

<p>In this approach based on the <b>description</b> of the item, the user is suggested an item. The decription can be any product detail like in our case it is the review of the tousism places. It provides very useful information about the item/place like whether it is a place of worship, fun, adventure etc. The format of these details are in string (text format) and is important to convert them.</p>

A tag is created using the concept of <b>Term Frequency-Inverse Document Frequency(TF-IDF).</b>

TF-IDF is used in Information Retrieval for feature extraction purposes and it is a sub-area of Natural language Processing(NLP).

Term Frequency- Frequency of the word in the current document to the total number of words in the document. It signifies the occurrence of the word in a document and gives higher weight when the frequency is more so it is divided by document length to normalize.

![image-2.png](attachment:image-2.png)

Inverse Document Frequency- Total Number of Documents to the frequency occurrence of documents containing the word. It signifies the rarity of the word as the word occurring the document is less the IDF increases. It helps in giving a higher score to rare terms in the documents.

![image-3.png](attachment:image-3.png)

TF-IDF is statistical measure that evaluates how relevant a word is to a document in a collection of documents.

TF-IDF for a word in a document is calculated by multiplying two different metrics:
<ul>
    <li>The term frequency of a word in a document(Tf)</li>
    <li>The inverse document frequency(idf) of a word across a set of documents. The closer it is 0, the more common a word is.</li>
</ul>****
