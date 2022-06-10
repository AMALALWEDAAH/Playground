from flask import Flask, render_template
# Create a new instance of the Flask class called "app"
app = Flask(__name__)


# The "@" decorator associates this route with the function immediately following
@app.route('/play/<num>')
def play_times(num, color="skyblue"):
    # Return the string 'Hello World!' as a response
    return render_template("index.html", _num=int(num), color=str(color))


@app.route('/play')
def play(num=3, color="skyblue"):
    # Return the string 'Hello World!' as a response
    return render_template("index.html", _num=int(num), color=str(color))


@app.route('/play/<num>/<string:color>')
def color(num, color):
    # Return the string 'Hello World!' as a response

    return render_template("index.html", _num=int(num), color=color)
    # return '''
    # <div class="box" style="--color: {{ color }};"></div>
    # '''


if __name__ == "__main__":   # Ensure this file is being run directly and not from a different module
    app.run(debug=True)    # Run the app in debug mode.
