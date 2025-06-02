from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    table = []
    error = None
    number = None

    if request.method == 'POST':
        try:
            number = int(request.form['number'])
            table = [(number, i, number * i) for i in range(1, 11)]
        except ValueError:
            error = "Please enter a valid number."

    # HTML template with placeholders
    html_template = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Multiplication Table Generator</title>
    </head>
    <body>
        <h1>Enter a Number to Print its Multiplication Table</h1>
        {% if error %}
            <p style="color: red;">{{ error }}</p>
        {% endif %}
        <form method="POST">
            <input type="text" name="number" placeholder="Enter a number" required>
            <input type="submit" value="Generate Table">
        </form>
        {% if table %}
            <h2>Multiplication Table for {{ number }}</h2>
            <table border="1" cellpadding="5" cellspacing="0">
                <tr>
                    <th>Number</th>
                    <th>Multiplier</th>
                    <th>Product</th>
                </tr>
                {% for n, i, product in table %}
                <tr>
                    <td>{{ n }}</td>
                    <td>{{ i }}</td>
                    <td>{{ product }}</td>
                </tr>
                {% endfor %}
            </table>
        {% endif %}
    </body>
    </html>
    """

    return render_template_string(html_template, table=table, number=number, error=error)

if __name__ == '__main__':
    app.run(host = "0.0.0.0", debug=True)
