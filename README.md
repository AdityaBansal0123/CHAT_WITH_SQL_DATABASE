🦜 Conversational AI-Powered SQL Query Interface
An interactive Streamlit-based web application that uses LangChain, LLaMA3 via Groq API, and SQLAlchemy to enable natural language interaction with SQL databases (SQLite & MySQL). Ask questions like "Show me all students in Data Science section A" and get answers in real-time.

🚀 Features
LLM-Powered Querying: Uses LLaMA3-8B-8192 model via Groq API to interpret and run SQL queries from natural language.

Dual Database Support: Seamlessly switch between a local SQLite3 (student.db) and remote MySQL database via UI.

Streamlit Interface: Intuitive web UI for chat-based interaction and real-time responses.

SQLDatabaseToolkit Integration: Efficient execution and handling of SQL logic using LangChain tools.

Session Management: Maintains chat history with a "Clear history" option.

Safe & Configurable: Inputs are protected and database access is read-only for SQLite.

🧱 Tech Stack
Frontend: Streamlit

Backend: Python, LangChain, SQLAlchemy

LLM: LLaMA3-8B-8192 via Groq

Databases: SQLite3 (student.db) and MySQL

🗂 Project Structure
bash
Copy
Edit
📁 your-project/
│
├── app.py             # Main Streamlit app
├── sqlite.py          # Script to create and populate sample student.db
├── student.db         # Sample SQLite3 database
🛠 Setup Instructions
Clone the repository:

bash
Copy
Edit
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name
Install dependencies:

nginx
Copy
Edit
pip install -r requirements.txt
Create and populate SQLite DB (optional):

nginx
Copy
Edit
python sqlite.py
Run the Streamlit app:

arduino
Copy
Edit
streamlit run app.py
Provide your Groq API Key and database credentials in the sidebar UI.

🧪 Example Queries
Show all students from section A

What is the average mark in Data Science?

List students with marks above 80

🔐 Security Notes
MySQL credentials and Groq API key are entered via sidebar and not hard-coded.

SQLite database is opened in read-only mode to prevent unwanted writes or deletions.
