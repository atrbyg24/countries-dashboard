# countries-dashboard
🌍 Global Country Data Dashboard
This is a simple Streamlit web application that allows users to explore and visualize various data points about countries worldwide. The data is fetched from the free and public REST Countries API.

✨ Features
Comprehensive Country Data: Displays official name, capital, region, subregion, population, area, and flag (emoji and URL) for a vast list of countries.

Interactive Filtering:

Search countries by common name, official name, or capital.

Filter countries by geographical region using a multi-select dropdown.

Population Visualization: A dynamic bar chart shows the population of the filtered countries, allowing for easy comparison.

Responsive Design: Built with Streamlit, ensuring a clean and responsive user interface.

🚀 How to Run Locally
To get this dashboard up and running on your local machine, follow these steps:

1. Prerequisites

Make sure you have Python 3.7+ installed.

2. Clone the Repository (or save the code)

# If this were a Git repository
git clone <your-repo-url>
cd <your-repo-name>

3. Install Dependencies

Install the required Python libraries using pip:

pip install streamlit pandas requests altair

4. Save the Code

Save the provided Python code (from the Canvas) into a file named app.py (or any other .py file).

5. Run the Streamlit App

Open your terminal or command prompt, navigate to the directory where you saved app.py, and run the following command:

streamlit run app.py

This command will start the Streamlit server, and your web browser will automatically open a new tab displaying the dashboard.

⚙️ API Used
This project utilizes the REST Countries API. Specifically, it uses the /v3.1/all endpoint with a fields parameter to fetch only the necessary data points, ensuring efficient data retrieval. This API is free and does not require an API key.

📄 License
This project is open-source and available under the MIT License.