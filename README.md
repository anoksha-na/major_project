# AI-Powered Medical Diagnosis Platform

An integrated AI-based platform for medical image classification and interactive chatbot assistance, designed to support healthcare professionals in diagnosing cancer and related conditions.  

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This project combines computer vision, natural language processing, and web technologies to build a complete medical assistance platform. It includes a customized ResNet model for cancer classification, a chatbot for medical guidance, and a Flask-based web application with user authentication and reporting features.  

## Features

- Image Classification  
  - Customized ResNet model for cancer detection and classification  
  - Supports training, testing, and evaluation of medical images  

- Interactive Chatbot  
  - NLP-powered chatbot trained on medical intents and knowledge  
  - Provides instant answers to health-related queries  

- Web Application  
  - Flask-based frontend with multiple pages: Home, Login, Dashboard, Chatbot, Reports, Results  
  - Secure user authentication with SQLite database  

- Report Generation  
  - Automatic medical diagnosis report generation in PDF format  

- Voice Assistant  
  - Module for voice-based interaction with the chatbot  

## Tech Stack

- Frontend: HTML, CSS, JavaScript  
- Backend: Flask (Python)  
- Machine Learning: TensorFlow, Keras (Custom ResNet, CNNs)  
- NLP: NLTK, intents.json knowledge base, trained chatbot model  
- Database: SQLite  
- Utilities: PDF generation, Voice Assistant integration  

## Project Structure

## Project Structure

```plaintext
major_project/
├── app1.py                  # Main Flask app
├── customised_renet_model.py # Customized ResNet for cancer classification
├── chatbott.py              # Chatbot implementation
├── chat_test.py             # Chatbot testing script
├── chatbot_model.h5         # Trained chatbot model
├── intents.json             # Chatbot intents
├── medical_knowledge.json   # Additional chatbot knowledge base
├── users.db                 # SQLite database
├── pdf.py                   # PDF report generator
├── vc_ass.py                # Voice assistant module
├── classes.pkl              # Saved class labels
├── words.pkl                # Saved tokenized words
├── writing.py               # Utility script
├── *.html                   # Frontend templates (home, login, dashboard, chatbot, report, result)
├── *.css                    # Stylesheets for UI
├── *.js                     # JavaScript files
├── i3.jpg / i4.png          # Sample assets
└── README.md                # Project documentation

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/anoksha-na/major_project.git
   cd major_project

pip install -r requirements.txt

