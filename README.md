# 📝 Expert Sentence Analyzer

A robust Natural Language Processing (NLP) web application that provides real-time linguistic insights. This tool breaks down sentences into their grammatical components, fetches lexical definitions, and evaluates readability using professional scoring algorithms.

---

## 🚀 Key Features

- **Grammatical Tagging**: Automatically identifies Parts of Speech (POS) using NLTK's `averaged_perceptron_tagger`.
- **Lexical Definition Lookup**: Integrates the **WordNet** database to provide "Simple Meanings" for each word in the sentence.
- **Readability Evaluation**: Implements the **Flesch Reading Ease** algorithm via the `textstat` library, mapped to a custom 1.0 - 5.0 complexity scale.
- **Interactive Audio**: Includes a built-in Text-to-Speech (TTS) feature using the Web Speech API to read analyzed sentences aloud.
- **Real-Time Data Table**: Utilizes the JavaScript **Fetch API** to process text and update the UI without reloading the page.

## 🛠️ Technical Stack

- **Backend**: Python 3.x, Flask
- **NLP Engine**: NLTK (Natural Language Toolkit), Textstat
- **Frontend**: HTML5, CSS3 (Flexbox), JavaScript (ES6+)
- **Data Repository**: WordNet Corpus

## 🔮 Useful Applications

(i) **Educational Support**: An interactive tool for language learners to visualize sentence structure and expand their vocabulary with instant definitions.

(ii) **Accessibility Aid**: Helps users with visual impairments or reading difficulties by providing audio playback of entered text.

(iii) **Content Writing & Editing**: Assists writers in ensuring their content is appropriately leveled for their audience by monitoring the readability score.

(iv) **Linguistic Analysis**: Provides a quick-access tool for students and researchers to perform basic syntactic analysis on specific phrases or sentences.
