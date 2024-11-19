# Fortis Virtual Assistant - Kasia

## Overview
This project creates **Kasia**, a virtual assistant for **Fortis Marketing Agency**, using **OpenAI API** and **Streamlit**. Kasia assists users by providing accurate and comprehensive information about Fortis' services and promotional activities (e.g., lotteries and contests). It utilizes file-based vector search to ensure precise responses.

---

## Features
1. **Virtual Assistant Creation**:
   - Automatically initializes Kasia if not already set up.
   - Configurable assistant instructions for consistent and professional behavior.
2. **File-Based Vector Search**:
   - Uses vector stores to organize and search promotional and service-related documents.
   - Handles large datasets with chunking and overlap for optimal data retrieval.
3. **Streamlit User Interface**:
   - Interactive chat interface for seamless user interaction.
   - Displays chat history and real-time assistant responses.
4. **Query Handling**:
   - Responds to diverse queries based on Fortis' data files.
   - Guides users through Fortis services and promotions with accurate and empathetic replies.
5. **Dynamic Context Management**:
   - Tracks conversation threads for maintaining context.
   - Supports concurrent threads for multiple users.

---

## Project Structure
- **`createassistant.py`**:
  - Creates the assistant with predefined instructions.
  - Initializes vector stores and uploads files for data retrieval.
- **`run.py`**:
  - Implements a Streamlit-based chatbot interface.
  - Manages user input, chat history, and assistant responses.
- **Promotional and Service Files**:
  - Includes 13 files (8 lottery files, 4 contest files, and 1 Fortis website data file).

---

## Prerequisites
1. **Python Version**: Python 3.9 or later.
2. **Required Libraries**:
   Install dependencies using:
   ```bash
   pip install -r requirements.txt
   ```

## Environment Variables:
1. **Create a .env file with:**
  - OPENAI_API_KEY=<your_openai_api_key>
  - ASSISTANT_ID=
  - VECTOR_STORE_ID=

## Setup and Usage
1. **Clone the Repository**
  - git clone <repository-url>
  - cd <repository-folder>

2. **Install Dependencies**
  - pip install -r requirements.txt

4. **Configure Environment**
  - Create a .env file:
  - OPENAI_API_KEY=<your_openai_api_key>

5. **Prepare Data Files**
  - Place the promotional and service-related files in the project directory or update their paths in createassistant.py.

6. **Initialize the Assistant**
  - Run the createassistant.py script to set up the assistant and upload files:
  - python createassistant.py

7. **Launch the Application**
  - Run the run.py script to start the Streamlit interface:
  - streamlit run run.py
  - Open the provided URL in your browser to interact with Kasia.
   
## Assistant Capabilities

### User Queries
- **Kasia provides**:
  - Information about Fortis services and promotions.
  - Support for both general and specific inquiries.
  - Responses are based solely on the uploaded files.

---

### Data Handling
- **File Types**: PDF files for promotional and service information.
- **Chunking Strategy**:
  - Chunks are created with a maximum size of 800 tokens and a 400-token overlap for enhanced search accuracy.

---

### Customization
#### Update Instructions
- Modify the assistant's behavior by editing the `instructions` parameter in `createassistant.py`.

#### Add/Update Files
- Update the `file_paths` list in `createassistant.py` to add or replace files.

#### UI Enhancements
- Customize the Streamlit interface in `run.py` for branding or additional features.

---

### Troubleshooting

#### Common Issues
1. **Assistant Not Responding**:
   - Verify `ASSISTANT_ID` is correctly stored in the `.env` file.
   - Ensure the OpenAI API key is active and valid.
2. **File Upload Errors**:
   - Confirm that the file paths in `createassistant.py` are correct.
   - Check that the files are in the expected format (PDF).
3. **Streamlit Errors**:
   - Clear the Streamlit cache:
     ```bash
     streamlit cache clear
     ```

#### Debugging Tips
- Use `print` statements in `createassistant.py` and `run.py` to track process execution.
- Ensure all required libraries are installed.

---

### Future Enhancements
1. Add multilingual support for non-English queries.
2. Enable real-time file uploads via the Streamlit UI.
3. Integrate analytics for tracking user interactions and assistant performance.
4. Expand functionalities to include more tools and dynamic updates.

---

### License
This project is licensed under the **MIT License**. See the `LICENSE` file for details.

---

### Contact
For queries or issues, contact [Your Name or Team] at [Your Email].
