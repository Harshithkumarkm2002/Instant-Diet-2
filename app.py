from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

# Load meal item data from JSON file
with open('static/data/meal_items.json', 'r') as f:
    meal_items = json.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/goals')
def goals():
    return render_template('goals.html')

@app.route('/plans/<goal>')
def show_diet_options(goal):
    if goal not in ['gain', 'loss']:
        return "Invalid goal", 404

    title = "Weight Gain & Bulking" if goal == 'gain' else "Weight Loss & Cutting"
    return render_template('diet_options.html', goal=goal, title=title)

@app.route('/plans/<goal>/<diet>')
def show_plan(goal, diet):
    template_name = f"{goal}_{diet}_plan.html"
    try:
        return render_template(template_name)
    except:
        return f"No plan found for {goal} - {diet}", 404

# New route for Customize Meal Plan
@app.route('/customize')
def customize():
    return render_template('customize.html')

# Serve item data as JSON for frontend
@app.route('/api/items')
def get_items():
    return jsonify(meal_items)

if __name__ == '__main__':
    app.run(debug=True)
