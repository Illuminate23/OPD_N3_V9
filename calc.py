from flask import Flask, request, render_template_string

app = Flask(__name__)

TEMPLATE = '''
<!doctype html>
<html lang="en">
<head>
    <title>Калькулятор сложного процента</title>
</head>
<body>
    <h1>Калькулятор сложного процента</h1>
    <form method="post">
        Начальная сумма (основная сумма): <input type="number" name="principal" step="any" required><br>
        Годовая процентная ставка (%): <input type="number" name="rate" step="any" required><br>
        Количество лет: <input type="number" name="time" step="any" required><br>
        Частота начисления процента в году: <input type="number" name="times_per_year" value="1" required><br>
        <input type="submit" value="Рассчитать">
    </form>
    {% if result %}
    <h2 id="result">Итоговая сумма: {{ result }}</h2>
    {% elif error %}
    <h2 id="error">{{ error }}</h2>
    {% endif %}
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def calculator():
    result = None
    error = None
    if request.method == 'POST':
        try:
            principal = float(request.form['principal'])
            rate = float(request.form['rate']) / 100
            time = float(request.form['time'])
            times_per_year = int(request.form['times_per_year'])
            if principal < 0 or rate < 0 or time < 0 or times_per_year < 1:
                raise ValueError("Все значения должны быть положительными, и частота начисления процента должна быть хотя бы 1.")
            
            amount = principal * (1 + rate / times_per_year) ** (times_per_year * time)
            result = round(amount, 2)
        except ValueError as e:
            error = str(e)
    
    return render_template_string(TEMPLATE, result=result, error=error)

if __name__ == '__main__':
    app.run(debug=True)
