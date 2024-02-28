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
    <h2>Итоговая сумма: {{ result }}</h2>
    {% endif %}
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def compound_interest_calculator():
    result = None
    if request.method == 'POST':
        principal = float(request.form['principal'])
        rate = float(request.form['rate']) / 100
        time = float(request.form['time'])
        times_per_year = int(request.form['times_per_year'])
        
        amount = principal * (1 + rate / times_per_year) ** (times_per_year * time)
        
        result = round(amount, 2)
        
    return render_template_string(TEMPLATE, result=result)

