# KITS Chatbot

Welcome to the KITS Chatbot application! This chatbot is designed to assist with inquiries about Krishna Chaitanya Institute of Technology & Sciences (KITS). It uses a natural language processing engine to respond to user queries and provides both text and voice interactions.

## Features

- **Text-Based Chat**: Communicate with the chatbot using text input.
- **Voice-Based Chat**: Interact with the chatbot using voice commands.
- **Text-to-Speech**: The chatbot can read responses aloud.
- **Save Chat History**: Save your conversation to a text file.
- **Clear Chat History**: Clear the chat history from the display.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install Required Libraries**:
   Make sure you have Python installed. Then, install the required libraries using pip:
   ```bash
   pip install tkinter nltk pyttsx3 speechrecognition
   ```

3. **Download NLTK Data**:
   You need to download the NLTK data for the chatbot to work correctly. Run the following commands in your Python environment:
   ```python
   import nltk
   nltk.download('punkt')
   ```

## Usage

1. **Run the Application**:
   ```bash
   python <script-name>.py
   ```

2. **Using the Chatbot**:
   - **Text Input**: Type your message in the entry box and press Enter or click the "Send" button.
   - **Voice Input**: Click the "Voice Input" button and speak your query.
   - **Clear Chat**: Click the "Clear Chat" button to clear the chat history.
   - **Save Chat**: Click the "Save Chat" button to save the conversation to a text file.

## Chatbot Commands

The chatbot can respond to a variety of queries related to KITS. Here are some examples:

- **Greetings**: "hi", "hello", "hey"
- **College Information**: "Branches?", "Departments?", "Admission requirements?", "Campus facilities?"
- **Events and Activities**: "Cultural events?", "Extracurricular opportunities?"
- **Administrative Info**: "Principal?", "CSE HOD?", "Chairman?"
- **General Queries**: "College location?", "College founded?", "Mission and vision?"

## Code Overview

- **Libraries Used**:
  - `tkinter`: For the GUI
  - `nltk.chat.util`: For creating the chatbot
  - `pyttsx3`: For text-to-speech conversion
  - `speech_recognition`: For handling voice input

- **Main Components**:
  - **Patterns and Responses**: Defined patterns and responses for the chatbot.
  - **Chat Object**: `Chat` object to handle conversation.
  - **Text-to-Speech Engine**: Initialized `pyttsx3` engine for TTS.
  - **Functions**:
    - `send_message()`: Handles user input and generates responses.
    - `clear_chat()`: Clears the chat history.
    - `save_chat()`: Saves the chat history to a file.
    - `voice_input()`: Handles voice input and processes it.
  - **Tkinter GUI**: Set up the main window, chat history, input entry, and buttons.

## Future Enhancements

- Improve the chatbot's natural language understanding capabilities.
- Add more patterns and responses for a wider range of queries.
- Implement more advanced voice recognition and TTS features.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

---

This README provides a comprehensive guide to setting up and using the KITS Chatbot. If you have any questions or need further assistance, feel free to reach out. Enjoy chatting with the KITS Chatbot!
