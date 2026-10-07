from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():

    strength = ""
    alert = ""
    suggestions = []
    common_password = ""

    weak_passwords = [
        "123456",
        "password",
        "12345678",
        "qwerty",
        "admin",
        "123456789",
        "111111"
    ]

    if request.method == "POST":

        password = request.form["password"]

        score = 0

        # Check common password
        if password.lower() in weak_passwords:
            common_password = "⚠️ This is a commonly used password."

        # Check length
        if len(password) >= 8:
            score += 1
        else:
            suggestions.append("Use at least 8 characters.")

        # Check uppercase
        if any(char.isupper() for char in password):
            score += 1
        else:
            suggestions.append("Add an uppercase letter.")

        # Check lowercase
        if any(char.islower() for char in password):
            score += 1
        else:
            suggestions.append("Add a lowercase letter.")

        # Check number
        if any(char.isdigit() for char in password):
            score += 1
        else:
            suggestions.append("Add a number.")

        # Check special character
        if any(not char.isalnum() for char in password):
            score += 1
        else:
            suggestions.append("Add a special character.")

        # Strength
        if score <= 2:
            strength = "Weak"
            alert = "Warning: Your password is weak!"

        elif score <= 4:
            strength = "Medium"

        else:
            strength = "Strong"

    return render_template(
        "index.html",
        strength=strength,
        alert=alert,
        suggestions=suggestions,
        common_password=common_password
    )


if __name__ == "__main__":
    app.run(debug=True)