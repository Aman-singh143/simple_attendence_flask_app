from flask import Flask, render_template, request
import datetime

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def attendance_form():
    success_message = ""

    current_date = datetime.datetime.now().strftime('%Y-%m-%d')
    current_time = datetime.datetime.now().strftime('%H:%M')

    if request.method == 'POST':
        student_name = request.form['student_name']
        student_id = request.form['student_id']

        with open('attendance_records.csv', 'a') as file:
            file.write(f'{student_name},{student_id},{current_date},{current_time}\n')

        success_message = "Form submitted successfully!"

    return render_template('attendance_form.html', success_message=success_message, current_date=current_date, current_time=current_time)

if __name__ == '__main__':
    app.run(debug=True)
