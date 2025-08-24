# Major Project: AI-Powered Medical Diagnosis Platform

An integrated AI-based platform for **medical image classification** and **interactive chatbot assistance**, designed to support healthcare professionals in diagnosing cancer and related conditions.  

## 🚀 Features

- **Image Classification**:  
  - Customized ResNet model for cancer detection and classification.  
  - Supports training, testing, and evaluation of medical images.  

- **Interactive Chatbot**:  
  - NLP-powered chatbot trained on medical intents and domain knowledge.  
  - Provides instant answers to health-related queries.  

- **Web Application**:  
  - Flask-based frontend with multiple pages: Home, Login, Dashboard, Chatbot, Reports, Results.  
  - Secure user authentication with SQLite database (`users.db`).  

- **Report Generation**:  
  - Automatic medical diagnosis report generation in PDF format.  

- **Voice Assistant**:  
  - Integrated module for voice-based interaction with the chatbot.  

## 🛠️ Tech Stack

- **Frontend**: HTML, CSS, JavaScript  
- **Backend**: Flask (Python)  
- **Machine Learning**: TensorFlow, Keras (Custom ResNet, CNNs)  
- **NLP**: NLTK, intents.json knowledge base, trained chatbot model  
- **Database**: SQLite (`users.db`)  
- **Utilities**: PDF generation, Voice Assistant integration  

## 📂 Project Structure

major_project/
│── app1.py # Main Flask app
│── customised_renet_model.py # Customized ResNet for cancer classification
│── chatbott.py / chat_test.py # Chatbot implementation
│── chatbot_model.h5 # Trained chatbot model
│── intents.json # Chatbot intents
│── medical_knowledge.json # Additional chatbot knowledge base
│── users.db # SQLite database
│── pdf.py # PDF report generator
│── vc_ass.py # Voice assistant module
│── *.html / *.css / *.js # Frontend files (UI, dashboard, login, chatbot, results)
│── classes.pkl / words.pkl # Saved tokenizer/encoder objects
│── i3.jpg / i4.png # Sample assets
