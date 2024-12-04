import pandas as pd
from flask import Flask, render_template_string

table = pd.read_csv("Table_Input.csv")

a = int(table.loc[table['Index #'] == 'A5', 'Value'].iloc[0]) + int(table.loc[table['Index #'] == 'A20', 'Value'].iloc[0])
b = int(table.loc[table['Index #'] == 'A15', 'Value'].iloc[0]) / int(table.loc[table['Index #'] == 'A7', 'Value'].iloc[0])
c = int(table.loc[table['Index #'] == 'A13', 'Value'].iloc[0]) * int(table.loc[table['Index #'] == 'A12', 'Value'].iloc[0])

app = Flask(__name__)

#HTML for site

html_template = """
<!DOCTYPE html>
<html>
<head>
    <title>Table Display</title>
</head>
<body>
    <h1>Table 1</h1>
    <table border="1" style="border-collapse: collapse; text-align: center;">
        <tr>
            <th>Index #</th>
            <th>Value</th>
        </tr>
        {% for index, value in table1 %}
        <tr>
            <td>{{ index }}</td>
            <td>{{ value }}</td>
        </tr>
        {% endfor %}
    </table>

    <h1>Table 2</h1>
    <table border="1" style="border-collapse: collapse; text-align: center;">
        <tr>
            <th>Category</th>
            <th>Value</th>
        </tr>
        <tr>
            <td>Alpha</td>
            <td>{{ alpha }}</td>
        </tr>
        <tr>
            <td>Beta</td>
            <td>{{ beta }}</td>
        </tr>
        <tr>
            <td>Charlie</td>
            <td>{{ charlie }}</td>
        </tr>
    </table>
</body>
</html>
"""

@app.route("/")

def main():
    table1 = table.values.tolist()
    return render_template_string(html_template, table1=table1, alpha=a, beta=b, charlie=c)

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000)) 
    app.run(host="0.0.0.0", port=port)
