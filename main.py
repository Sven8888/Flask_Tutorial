from flask import Flask, render_template

app = Flask(__name__)

# Sample data (replace this with your actual data)
items = [
    "Dream City", "Wanderlust Valley", "Fantasy Isle", "Mystic Woods",
    "Whispering Falls", "Eternal Springs"
]


@app.route("/")
def home():
  # Prepare the context to pass to the template
  context = {'items': items}

  # Render the "home.html" template with the context
  return render_template('home.html', **context)


# -----------get ip address, create a cookie and redirect to another path --------------
#user_ip = request.remote_addr
#response= make.response(redirect("/other_folder"))
#response.set_cookie("user_ip", user_ip)
#return response

#user_ip_get= request.cookies.get("user_ip")


app.run(host='0.0.0.0', port=5000, debug=True)
#if __name__ == '__main__':
#  app.run(debug=True)
