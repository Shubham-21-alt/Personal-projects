#!/usr/bin/env python
# coding: utf-8

# In[20]:


import re
import spacy

# Load spaCy English model
nlp = spacy.load("en_core_web_sm")

def read_text_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()
    return text

def clean_sentence(sentence):
    sentence = sentence.lower()
    sentence = re.sub(r"\s+", " ", sentence)  # Normalize whitespace
    sentence = re.sub(r"[\n\r\t]", " ", sentence)  # Remove newlines/tabs
    sentence = re.sub(r" +", " ", sentence)  # Remove repeated spaces
    sentence = sentence.strip()
    return sentence

def preprocess_text(filepath):
    raw_text = read_text_file(filepath)
    doc = nlp(raw_text)
    sentences = [sent.text for sent in doc.sents]
    cleaned_sentences = [clean_sentence(s) for s in sentences if len(s.strip()) > 3]
    return cleaned_sentences



# In[22]:


if __name__ == "__main__":
    test_path = "C:\\Users\\Dell\\Desktop\\legal-trap-detector\\data\\sample_input.txt"  # Make sure this file exists with some text
    result = preprocess_text(test_path)
    print("📄 Cleaned Sentences:")
    for sentence in result:
        print("-", sentence)


# In[ ]:





# In[ ]:






# In[ ]:






# In[ ]:




