from flask import Flask
from flask import render_template

app = Flask(_name_, template_folder='templates')

@app.route("/")
def url_principal():
	return render_template("template.html", nombre="Jorge Alberto Lopez Barboza", escuela="Tecnologico de Guanajuato", carrera="Ingenieria en Sistemas Computacionales", semestre="8vo Semestre");
	

@app.route("/skills")
def skills():
	return render_template("skills.html");

@app.route("/education")
def education():
	return render_template("education.html");

if __name__ == "__main__":
	app.run(debug=True)


