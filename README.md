# Trade Data Analysis Dashboard :coin:

This ML-Based Trade Data Analysis Dashboard is built using Python, Plotly, and Dash. It allows you to interactively visualize and analyze trade data trends, detect anomalies, and explore summary statistics of the trade data.

## Features

- **Trade Data Trends**: The dashboard displays line plots to visualize the trends of various trade data metrics (e.g., import value, export value, total trade value) over the years.

- **Detected Anomalies**: An interactive scatter plot is provided to visualize the detected anomalies in the trade data. Anomalies are indicated by different colors, and you can hover over the data points to view the reconstruction error.

- **Trade Data Summary**: The dashboard presents a summary table that includes statistics and aggregated values of the trade data, providing a quick overview of the data distribution.

## Usage

1. Install the required dependencies listed in the `requirements.txt` file using the command: `pip install -r requirements.txt`.

2. Update the code with your specific trade data and anomalies. Make sure to replace `trade_data` and `anomalies` with your own data.

3. Run the dashboard by executing the Python script. Use the command: `python app.py`. The dashboard will be hosted on a local server (usually http://127.0.0.1:8050/).

4. Access the Trade Data Analysis Dashboard in your web browser by visiting the specified local host address.

## Customization

- You can modify the code to incorporate additional features and visualizations based on your specific requirements. Refer to the Dash and Plotly documentation for more information on available components and customization options.

- Update the front-end layout by adjusting the styles and HTML components in the `app.layout` section to match your desired design.

## Dependencies

- Python 3.7 or higher
- Dash 1.21.0 or higher
- Plotly 5.3.1 or higher
- pandas 1.3.3 or higher

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

