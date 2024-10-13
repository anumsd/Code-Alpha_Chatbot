# Code-Alpha_Chatbot
# Chatbot with TF-IDF and Cosine Similarity

## Overview
This project is a basic chatbot built using Python and natural language processing techniques. It responds to user queries by recognizing greetings, providing predefined responses, or using TF-IDF (Term Frequency-Inverse Document Frequency) and cosine similarity to generate context-aware replies. The chatbot can handle simple questions and conversations, including topics like weather, jokes, and recommendations.

## Features
- **Greeting Recognition**: The bot detects common greetings such as "hello" or "hi" and responds with random friendly replies.
- **Predefined Responses**: The bot has a set of fixed responses for specific queries like "How are you?" or "Tell me a joke."
- **Cosine Similarity Matching**: For questions not covered by fixed responses, the chatbot uses a TF-IDF model and cosine similarity to find the closest matching response from its knowledge base.
- **Fallback Responses**: If the chatbot is unable to find a relevant answer, it provides a polite fallback response asking for clarification.
- **Exit Option**: The chatbot conversation can be ended anytime by typing "bye."

## How It Works
1. **Corpus and Tokenization**: The chatbot has a predefined set of sentences (corpus) stored as sample conversation lines. The corpus is tokenized using the `spaCy` library.
2. **Greeting Function**: The `greeting()` function checks if the user's input contains any common greeting words. If so, it randomly chooses a response from a list of greeting replies.
3. **Custom Responses**: The `customresponse()` function provides predefined answers for commonly asked questions like "Who created you?" or "What's the weather today?"
4. **TF-IDF Similarity**: The `functionresponse()` function calculates the cosine similarity between the user's input and the chatbot's corpus using a TF-IDF vectorizer. It returns the most similar response or a fallback if the similarity score is too low.
5. **Conversation Loop**: The main `chatbot()` function keeps the conversation going until the user types "bye" to exit the chat.

## Dependencies
- Python 3.6+
- `spaCy` library for natural language processing.
- `sklearn` (Scikit-learn) library for TF-IDF vectorization and cosine similarity calculations.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/chatbot.git
   ```
2. Navigate to the project directory:
   ```bash
   cd chatbot
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   **Note**: The dependencies will include `spacy` and `scikit-learn`.

4. Download the `spaCy` language model:
   ```bash
   python -m spacy download en_core_web_sm
   ```

## Usage
To start the chatbot, run the following command:
```bash
python chatbot.py
```
The chatbot will greet you and respond to your input. Type "bye" to exit the conversation.

## Example Interaction
```
Bot: Hey! I am your chatbot assistant. To exit, type 'Bye' or 'bye'.
You: Hello
Bot: Hi
You: Tell me a joke
Bot: Why don't scientists trust atoms? Because they make up everything!
You: What's the weather today?
Bot: The weather today is sunny with a high of 25°C. Perfect day for a walk!
You: bye
Bot: Bye! Nice to meet you!
```

## Customization
You can expand or customize the chatbot by adding new predefined responses to the `response_fixed` dictionary or modifying the `corpus` with additional conversation topics.

## License
This project is open-source and available under the MIT License. Feel free to contribute or modify as per your needs!
