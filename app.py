from flask import Flask, render_template, request, redirect, url_for, flash
import smtplib

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        email = request.form['email']
        message = request.form['message']

        try:
            # Send email (use your email logic here)
            # Example (this needs to be configured with proper credentials)
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login('ridhampatel0510@gmail.com', 'okdh tpqs iwnf psrm')
            server.sendmail('ridhampatel0510@gmail.com', email, message)
            server.quit()

            flash('Email sent successfully!', 'success')
        except Exception as e:
            flash(f'Failed to send email: {str(e)}', 'error')

        # 🛑 Prevent resending on refresh
        return redirect(url_for('home'))

    return render_template('emailsender.html')

if __name__ == '__main__':
    app.run(debug=True)
