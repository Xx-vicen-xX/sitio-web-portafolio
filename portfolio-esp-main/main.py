from flask import Flask, render_template, request, flash, redirect, url_for
from flask_mail import Mail, Message

app = Flask(__name__)
app.secret_key = 'clave-secreta-segura'  # Necesaria para mostrar mensajes flash

# Configuración de Flask-Mail para Gmail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'vicentee777.777@gmail.com'
app.config['MAIL_PASSWORD'] = 'no-es-contraseña'  # No uses tu contraseña normal

mail = Mail(app)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        email = request.form["email"]
        text = request.form["text"]

        msg = Message("Nuevo mensaje de feedback",
                      sender=email,
                      recipients=["vicentee777.777@gmail.com"])
        msg.body = f"Correo: {email}\n\nMensaje:\n{text}"
        try:
            mail.send(msg)
            flash("¡Gracias por tu mensaje! Te responderé pronto.")
        except Exception as e:
            flash("Hubo un error al enviar el mensaje. Inténtalo más tarde.")
    
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)