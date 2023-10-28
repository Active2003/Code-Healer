from flask import Flask, render_template, request
import openai

app = Flask(__name__)

# Set your OpenAI API key
api_key = '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'  # Replace with your OpenAI API key

# Function to generate code suggestions
def generate_code_suggestions(user_code):
    openai.api_key = api_key
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"Provide code suggestions for the following code:\n\n{user_code}\n\nSuggestions:",
        max_tokens=50  # Adjust the number of tokens as needed
    )
    return response.choices[0].text

@app.route('/', methods=['GET', 'POST'])
def code_review():
    feedback = None

    if request.method == 'POST':
        user_code = request.form['code']
        suggestions = generate_code_suggestions(user_code)

        feedback = suggestions if suggestions else 'No feedback provided.'

    return render_template('index.html', feedback=feedback)

if __name__ == '__main__':
    app.run(debug=True)
