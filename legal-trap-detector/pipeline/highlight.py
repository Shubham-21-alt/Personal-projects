#!/usr/bin/env python
# coding: utf-8

# In[7]:


import os

def highlight_sensitive_clauses(cleaned_sentences, matches, output_path="C:\\Users\\Dell\\Desktop\\legal-trap-detector\\output\\flagged_output.html"):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Extract only the sentences that were matched
    matched_sentences = {match["sentence"] for match in matches}

    with open(output_path, "w", encoding="utf-8") as f:
        f.write("<html><head><meta charset='utf-8'><title>Flagged Legal Document</title></head><body>\n")
        f.write("<h2>📄 Legal Document</h2>\n")
        f.write("<p><i>Only sensitive sentences are highlighted below.</i></p><hr>\n")

        for sentence in cleaned_sentences:
            clean_sentence = sentence.strip()
            if clean_sentence in matched_sentences:
                f.write(f"<p><span style='background-color: yellow'>{clean_sentence}</span></p>\n")
            else:
                f.write(f"<p>{clean_sentence}</p>\n")

        f.write("</body></html>")




# In[8]:


if __name__ == "__main__":
    # Sample input sentences (simulating preprocessed output)
    input_sentences = [
        "This agreement will automatically renew every year unless cancelled in writing.",
        "Thank you for choosing our service.",
        "We reserve the right to modify these terms without notice.",
        "Contact us if you have any questions.",
    ]

    # Simulate matches (output from matcher)
    matches = [
        {"sentence": "This agreement will automatically renew every year unless cancelled in writing.", "matched_trap": "...", "similarity": 0.83},
        {"sentence": "We reserve the right to modify these terms without notice.", "matched_trap": "...", "similarity": 0.81},
    ]

    # Call the highlighter function
    highlight_sensitive_clauses(input_sentences, matches)

    print("✅ Test HTML generated at: output/flagged_output.html")

