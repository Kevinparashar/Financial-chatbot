# Financial Intelligence Chatbot

A robust, scalable chatbot system designed to process financial documents, extract insights, and answer user queries based on uploaded data.

## Overview

The Financial Intelligence Chatbot enables users to:
- Upload financial documents (CSV, Excel, PDF, DOCX)
- Ask questions in natural language
- Receive insights, visualizations, and analysis
- Compare data points and extract trends
- Translate responses to different languages

The system automatically detects the query intent and invokes the appropriate processing tool, ensuring a seamless user experience.

## Features

- **Multi-format Document Processing**: Handles CSV, Excel, PDF, and DOCX files
- **Intelligent Query Understanding**: Detects user intent from natural language questions
- **Automated Tool Selection**: Chooses the right processing method based on query type
- **Data Analysis & Visualization**: Generates statistics and visual representations of financial data
- **Text Summarization**: Extracts key points from lengthy documents
- **Web Content Integration**: Retrieves and summarizes information from URLs
- **Multilingual Support**: Detects languages and provides translation
- **Conversation History**: Maintains a log of all interactions for reference

## Demo

![Chatbot Demo](docs/images/demo.png)

*Example interaction with the chatbot analyzing financial data*

## Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Setup Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/financial-intelligence-chatbot.git
   cd financial-intelligence-chatbot
   ```

2. **Create and activate a virtual environment (recommended)**
   ```bash
   # On Windows
   python -m venv venv
   venv\Scripts\activate
   
   # On macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Create necessary directories**
   ```bash
   mkdir -p history
   ```

## Usage

1. **Start the application**
   ```bash
   streamlit run app.py
   ```

2. **Access the interface**
   - Open your web browser and go to http://localhost:8501
   - You'll see the Financial Intelligence Chatbot interface

3. **Upload a document**
   - Click the file upload area to select a financial document (CSV, Excel, PDF, or DOCX)

4. **Ask questions**
   - Type your question in the text box
   - Examples:
     - "Summarize this document"
     - "What's the average revenue?"
     - "Create a chart showing profit trends"
     - "Compare Q1 and Q2 expenses"

## Example Questions by Document Type

### For CSV/Excel Files
- "What's the average revenue in this dataset?"
- "Show me a chart of monthly expenses"
- "Compare the first and last quarter results"
- "What's the highest profit margin in this data?"

### For PDF/DOCX Files
- "Summarize this financial report"
- "What are the key points in this document?"
- "Extract information about projected growth"

### For Any Document
- "Translate this to Spanish"
- "Summarize the financial news from this URL: [link]"


## Technologies Used

- **Streamlit**: Web interface
- **Pandas**: Data processing
- **PyPDF2**: PDF parsing
- **python-docx**: DOCX parsing
- **Matplotlib**: Data visualization
- **BeautifulSoup**: Web content extraction
- **googletrans**: Translation service
- **langdetect**: Language detection

## Extending the System

The chatbot is designed with modularity in mind, making it easy to extend:

1. **Add New File Types**: Update `file_handler.py` with new format parsing
2. **Create New Tools**: Add new tools to the `tools/` directory
3. **Enhance Intent Detection**: Modify `query_handler.py` to recognize more intents

See the documentation in the `docs/` folder for detailed instructions on extending functionality.

## License

[MIT License](LICENSE)

## Contact

For questions or feedback, please contact [your-email@example.com].
