This project is a simple chatbot with a Tkinter GUI that fetches answers from documentation sources like Segment, mParticle, Lytics, and Zeotap based on user queries. The chatbot is designed to be run in a graphical user interface (GUI) window.

Features
Interactive GUI using Tkinter.
Fetches answers from documentation websites based on the user's query.
Supports basic queries related to setting up sources, creating profiles, building audience segments, and integrating data.
Postman was used to test API requests and ensure the chatbot fetches the correct content from documentation.
Requirements
Python 3.x (Tkinter is included in Python by default).
Libraries:
requests
beautifulsoup4
Installation
Step 1: Clone the Repository (Optional)
If you want to clone the project from GitHub, run the following command:

bash
Copy
Edit

cd chatbot-with-documentation-fetcher
Step 2: Install Required Libraries
You need to install requests and beautifulsoup4 to enable web scraping. Open your terminal or command prompt and run the following commands:

bash
Copy
Edit
pip install requests beautifulsoup4
Note: Tkinter is bundled with Python, so no separate installation is required for Tkinter.

Step 3: Save the Python Script
Ensure you have the Python script (chatbot_gui.py) saved on your local machine.

Step 4: Run the Application
Once the required libraries are installed, you can run the script.

Open Terminal/Command Prompt:

Windows: Press Win + R, type cmd, and press Enter.
macOS/Linux: Open your terminal.
Navigate to the Directory where you saved the chatbot_gui.py file.

Example (for Windows):

bash
Copy
Edit
cd C:\path\to\your\project
Run the Script:

For Python 3.x:
bash
Copy
Edit
python chatbot_gui.py
The GUI window will open, and you can interact with the chatbot.

Usage
Ask Questions: Type your question in the text field. Here are some examples:

"How do I set up a new source in Segment?"
"How can I create a user profile in mParticle?"
"How do I build an audience segment in Lytics?"
"How can I integrate my data with Zeotap?"
Click "Send": After typing your question, click the "Send" button.

View Answer: The answer fetched from the relevant documentation will appear in the answer box below.

Example Questions
Segment Documentation:
"How do I set up a new source in Segment?"
mParticle Documentation:
"How can I create a user profile in mParticle?"
Lytics Documentation:
"How do I build an audience segment in Lytics?"
Zeotap Documentation:
"How can I integrate my data with Zeotap?"
Testing with Postman
During development, Postman was used to test API requests and simulate the behavior of fetching documentation content from the respective websites. By setting up requests to these documentation URLs and inspecting the responses, the chatbot's scraping functionality was validated and refined.

Steps in Postman:

Set the API Endpoint: Use the URLs for each documentation source.
Send GET Requests: Test how the chatbot fetches content by making GET requests.
Inspect Responses: Ensure the content is correctly returned and extracted, simulating the behavior in the chatbot.
Troubleshooting
Tkinter Window Not Appearing:
Ensure that you have Python and Tkinter installed. If Tkinter is not available, install it:
On Windows: pip install tk
On macOS/Linux, Tkinter is typically included with Python but may need to be installed through a package manager.
Content Not Loading:
Make sure you have an active internet connection for the web scraping functionality.
If the structure of the documentation sites changes, you may need to update the web scraping logic.
Customization
You can customize this chatbot by:

Adding more platforms to the documentation_urls dictionary.
Modifying the answer_question() function to handle more types of questions.
Enhancing the GUI layout and appearance.
License


Summary of the Setup Process
Install the required libraries: requests and beautifulsoup4.
Save the Python script (chatbot_gui.py) to your local machine.
Run the script with python chatbot_gui.py.
Ask questions and interact with the chatbot in the GUI.
