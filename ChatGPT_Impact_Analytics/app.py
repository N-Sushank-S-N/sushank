from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dummy Data for Sections
feedback_data = {
    "ID": 1,
    "outcome_status": "resolved",
    "quality_of_answers": "good",
    "sentiment_score": 4.5,
    "satisfaction_level": 4,
    "free_form_feedback": "Great interaction!",
    "session_id": 12345
}

impact_metrics = {
    "category": "education",
    "before_score": 60,
    "after_score": 85
}

aggregated_feedback = {
    "sentiment_scores": 4.3,
    "satisfaction_breakdown": {
        "very_satisfied": 60,
        "satisfied": 30,
        "neutral": 10
    },
    "total_interactions": 100
}

usage_analytics = {
    "total_sessions": 150,
    "average_session_duration": "15 mins",
    "popular_use_cases": ["education", "business"]
}

domain_outcomes = {
    "education": "Grade improvements: +20%",
    "business": "Issue resolution time: decreased by 30%"
}

real_time_sentiment = {
    "sentiment_score": 4.7,
    "user_satisfaction_score": 90,
    "session_progress": "In Progress"
}

# Hardcoded username and password
USERNAME = 'testuser'
PASSWORD = 'password123'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Simple authentication check
        if username == USERNAME and password == PASSWORD:
            return redirect(url_for('dashboard'))  # Redirect to dashboard if login is successful
        else:
            error_message = "Invalid username or password"
            return render_template('login.html', error=error_message)  # Show error if login fails

    return render_template('login.html')  # Show login form if it's a GET request

@app.route('/register', methods=['GET', 'POST'])
def register():
    return render_template('register.html')  # You can add registration logic here

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html', feedback=feedback_data, impact_metrics=impact_metrics,
                           aggregated_feedback=aggregated_feedback, usage_analytics=usage_analytics,
                           domain_outcomes=domain_outcomes, real_time_sentiment=real_time_sentiment)

if __name__ == '__main__':
    app.run(debug=True)
