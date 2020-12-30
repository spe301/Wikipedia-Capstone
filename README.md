# Wikipedia-Protection-with-nlp


## Overview


<img src="Images/download.jpg/">
Wikipedia, as the name implies, is the Encyclopedia of the 21st century! It is an amazing place full of free information mantained by a community of volenteer editors. It has assisted in the removal of barriers when it comes to giving and receiving knwoledge. Unfortunatley, with this great democritization comes the potential spread of misinformation and plagarized content. With the rise of complex transformer models such as GPT2, AI can generate persuasive content that is practically identical to human written text.

See what I mean!: https://techcrunch.com/2019/02/17/openai-text-generator-dangerous/

This is where machine learning can help! We can train a Machine learning model to classify whether or not a body of text has been written by a human or an AI and use other NLP strategies to catch plagarism. If this seems like a problem you care about then keep reading!


If this project interests you feel free to shoot me an email via aacjpw@gmail.com

## Obtaining and Cleaning Data
Utimatley the dataset is a collection of 1,000 real Wikepedia articles and 1,000 AI generated articles. In Order to generate the articles I trained OpenAI's GPT2 on the set of real articles which were obtained by scraping Wikipedia with the BeautifulSoup library. I also had to remove many unknown character tags in order for the data to be "ML friendly".

## Generative Model
As mentioned earlier, I generated the fake articles with GPT2, a massive pre-trained neural network with a state of the art transformer architecture, to be more specific I used the 355M parameter version as the smaller 117M is best for datasets under 10MB. This process was fairly simple as the model was already built for me, however I did have to downgrade to tensorflow 1.15 because GPT2 is dependant on the tf.contrib module which dosen't exist in tensorflow 2. I also had to upgrade to colabs pro in order to have enough ram to train the model and generate all the text.

## Classification Model

## Bringing it to life with StreamLit
