# Recloset-AI-LLM

## Project Overview

* **Project Name**: Recloset-AI-LLM

* **Description**: An AI-based damage recognition and solution guidance system. This Flask server application receives image-based damage type recognition results and provides suitable solutions to users through LLM-based text generation using the Gemini API.

* **Key Features**:

*Text generation based on image damage type recognition results using LLM

*Handling user requests via a Flask server

*Deployment using Docker



## File Structure Description

* **Dockerfile**: Configuration file for building the Docker image / installs Flask server and required libraries

* **README.md**: Project introduction and usage guide

* **recloset_llm.py**: Main Flask server code / processes damage recognition and provides solution guidance via Gemini API

* **recloset_prompt.txt**: LLM prompt configuration file / instructions passed to the Gemini API

* **recloset_solution.xlsx**: Excel file summarizing solutions for each damage type

* **requirements.txt**: List of required Python packages for running the project

* **templates/index.html**: Web interface template


## Installation & Execution Guide

### Using Docker

1. Check Docker installation:

   ```bash
   docker --version
   ```
2. Build Docker image:

   ```bash
   docker build -t recloset-ai-llm .
   ```
3. Run Docker container:

   ```bash
   docker run -d -p 5000:5000 recloset-ai-llm
   ```

## Local Execution

1. Set up Python environment:

   ```bash
   python -m venv venv
   source venv/bin/activate
   ```
2. Install packages:

   ```bash
   pip install -r requirements.txt
   ```
3. Run Flask server:

   ```bash
   python recloset_llm.py
   ```

## How to Use

1. Access http://localhost:5000 in your web browser


2. Upload an image to analyze the damage type and receive a solution


3. Guidance for each damage type is based on the content of the recloset_solution.xlsx file



## API Endpoints

*'/': Server status check (GET)
*'/process_damage': Process damage type (POST)

  

  * Example JSON request:

    ```json
    { "damage_type": "1" }
    ```
  * Example response:

    ```json
    {  "response": "LLM-generated guidance text via Gemini API",
  "solution": "Predefined damage solution"  }
    ```


