## Exam Question

### Provide short answers to the questions below (1 paragraph at most):

**Given the sentence "I live near the bank of America", how can I get a:
	a. Contextualised word embedding of token 'bank'?
	b. Sentence embedding of the whole sequence.**
	
a. To obtain a contextualized word embedding for the token 'bank' from the sentence "I live near the bank of America", you would typically use models like BERT, ELMO, or RoBERTa. These models generate embeddings that take into account the surrounding words, unlike traditional embeddings like Word2Vec or GloVe which provide a fixed representation for each word. In this case, the word 'bank' would likely get an embedding representing a physical location rather than a financial institution due to the surrounding context.

b. For a sentence embedding of the entire sequence, you can again use models like BERT or its variants. Instead of extracting the embedding of a specific token, you would typically take the embedding of the special [CLS] token (in the case of BERT) as it's designed to hold sentence-level representations. Alternatively, models like Sentence-BERT (SBERT) or Universal Sentence Encoder (USE) are specifically designed for generating sentence embeddings and can provide a dense vector representation for the entire sequence.

---

### Explain the differences in training encoder-decoder (e.g. BERT), decoder-based (e.g. GPT) and encoder-decoder (e.g. T5)

1. **Encoder-Based**: In encoder-based architectures, the primary objective is to compress the input data into a fixed-size representation or context vector. This representation captures the crucial features of the input. Autoencoders are a prime example, where they aim to reduce input data into a lower-dimensional representation and often used for dimensionality reduction or feature learning.

2. **Decoder-Based**: Decoder-based models are primarily focused on generating or outputting data from a given representation. Given some context or encoded representation, the decoder's job is to produce a sequence or other structured data. In isolation, decoder-based structures are often utilized for tasks like image captioning where the input is a fixed-size feature vector from an image, and the output is a sequence of words.

3. **Encoder-Decoder**: An encoder-decoder architecture combines the two aforementioned structures. The encoder compresses the input into a fixed-size context vector, and the decoder then uses this representation to produce a sequence or other structured output. This architecture is predominantly used in tasks like machine translation, where an input sequence (sentence in source language) is encoded into a context, and a decoder generates an output sequence (translated sentence in the target language).

---

### Explain 2 ways to perform parameter-efficient finetuning

1. **Knowledge Distillation**: This technique involves training a smaller student model to mimic the behavior of a larger, pre-trained teacher model. During finetuning, the student model learns by trying to match the output distributions or representations of the teacher model rather than directly from the raw data. By doing this, the student model can achieve comparable performance with fewer parameters, making the finetuning process more efficient.

2. **Sparse Finetuning**: Instead of updating all parameters during the finetuning process, sparse finetuning selectively updates a subset of parameters. Techniques such as pruning can be used to identify and retain only the most important weights or connections in the network. After pruning, the remaining sparse model can be finetuned further, ensuring that only the most impactful parameters are updated and leading to more efficient use of resources.

---

### Explain 2 ways to make sure data quality is good when we're constructing a new NLP dataset

1. **Expert Review and Annotation Guidelines**: Engaging subject matter experts to review and annotate the data ensures that the dataset is both accurate and relevant. Providing clear annotation guidelines helps in maintaining consistency across different annotators. Regularly conducting inter-annotator agreement studies can further ensure that different annotators understand and follow the guidelines similarly, thus highlighting any potential ambiguities or sources of inconsistency in the data.

2. **Data Cleaning and Preprocessing**: Automated data cleaning processes can help identify and rectify common issues such as missing values, duplicates, or outliers. For NLP datasets specifically, preprocessing steps such as tokenization, stemming, and removal of stop words can be used. Additionally, employing techniques to detect and correct spelling or grammar errors, and ensuring balanced class distribution (in case of labeled data) can greatly enhance the quality of the dataset.

---

### Provide a detailed answer to the question below. Motivate your design choices and comment on the assumptions on resources available.

**I want to build a new model that reads a topic string as an input (e.g. "computer scientists"), and can write funny jokes about the topic. The input is free-text, i.e. users can ask whatever topics that would like. Let's assume that currently there's no dataset for this task at all. What is your solution to build this model?**

**Specifically, your answer must explain:**

 - **What kind of model will you use and why?**
 - **How would you train your model?**
 - **How would you evaluate your model?**
 - **What would be the potential weakness of your approach?**

<br>

**1. What kind of model will you use and why?**

Given the current advancements in Natural Language Processing (NLP), I would recommend using a transformer-based model, specifically one based on the GPT (Generative Pre-trained Transformer) architecture. The reason for this is threefold:

- **Transfer Learning**: GPT-based models come with a large amount of general knowledge from their pre-training on vast text datasets. This allows them to understand context, word relationships, and even some humor from their prior knowledge.
  
- **Flexibility**: The GPT model is designed for generative tasks, which means it can generate text (like jokes) based on the input provided.
  
- **Fine-tuning Ability**: While the pre-trained knowledge is vast, it can be fine-tuned to specific tasks. This would be beneficial for our specific requirement of generating jokes based on a topic.

**2. How would you train your model?**

Given there is no dataset available for this task, we need to be creative:

- **Data Collection**:
  1. **Web scraping**: You can scrape popular joke websites or platforms like Reddit's r/Jokes to gather a general dataset of jokes.
  2. **Crowdsourcing**: Use platforms like Amazon Mechanical Turk or similar to gather topic-specific jokes. Instruct the contributors to write jokes based on specific topics you provide or allow them to choose topics themselves.
  
- **Preprocessing & Augmentation**:
  - Clean the scraped data by removing any HTML tags, duplicates, or non-relevant content.
  - Augment the dataset by rephrasing existing jokes or slightly changing their structure while maintaining their meaning. This can give some variety.

- **Fine-tuning**:
  - Using the gathered dataset, fine-tune the pre-trained GPT model. The input would be the topic, followed by a prompt, and the output would be the corresponding joke.

**3. How would you evaluate your model?**

- **Quantitative Evaluation**:
  1. **BLEU Score**: Although more common for translation tasks, the BLEU score can be used to check if the generated joke is close to any human-written jokes in our dataset for the same topic.
  2. **Perplexity**: Measures how well the probability distribution predicted by the model aligns with the actual distribution of the words in the jokes.

- **Qualitative Evaluation**:
  1. **Human Evaluators**: Conduct user studies where participants rate the funniness and relevance of the generated jokes on a scale.
  2. **A/B Testing**: If integrating into a platform, you can perform A/B tests, where some users see model-generated jokes and others see human-written ones, and compare engagement metrics.

**4. What would be the potential weakness of your approach?**

- **Subjectivity of Humor**: What's funny for one person might not be for another. The model might generate jokes that are funny in a dataset context but not in real-world scenarios.
  
- **Safety and Ethical Concerns**: Relying on web-scraped data might introduce biases or generate inappropriate jokes. It's essential to implement post-generation filters or safety checks.
  
- **Overfitting**: If the dataset is not diverse enough, the model might overfit and generate very similar jokes for different topics.
  
- **Dependency on Dataset Quality**: The model is as good as the data it's trained on. If the scraped jokes or crowdsourced jokes are of poor quality, the model will generate poor jokes.

To conclude, the process of building such a model is iterative. You'll need to constantly refine the dataset, retrain the model, and evaluate its performance to achieve the best results.