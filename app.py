from flask import Flask, render_template, request, redirect, session
from flask_mysqldb import MySQL
import config

from models.user import User
from models.ad import Advertisement
from models.click import ClickTracker

app = Flask(__name__)
app.config.from_object(config)

mysql = MySQL(app)

@app.route('/')
def home():
    return redirect('/login')

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM users WHERE email = %s AND password = %s", (email, password))
        user = cursor.fetchone()
        cursor.close()

        if user:
            session['user'] = email  # 🔵 ¡IMPORTANTE! Guarda sesión aquí
            return redirect("/ads")
        else:
            return render_template("login.html", error="Credenciales inválidas")

    return render_template("login.html")


@app.route('/verify', methods=['POST'])
def verify():
    email = request.form['email']
    password = request.form['password']

    cursor = mysql.connection.cursor()
    user = User(None, email, password)
    if user.authenticate(cursor):
        session['user_id'] = user.id
        return redirect('/ad')
    else:
        return "Login incorrecto", 401

@app.route('/ad')
def ad():
    if 'user_id' not in session:
        return redirect('/login')

    cursor = mysql.connection.cursor()
    anuncios = Advertisement.get_all(cursor)
    cursor.close()

    return render_template('ad.html', ads=anuncios)


@app.route('/admin')
def admin_panel():
    cursor = mysql.connection.cursor()
    cursor.execute("""
        SELECT ads.title, COUNT(clicks.id) as total_clicks, SUM(ads.pay_per_click) as total_earned
        FROM clicks
        JOIN ads ON clicks.ad_id = ads.id
        GROUP BY ads.id
    """)
    results = cursor.fetchall()
    cursor.close()

    stats = []
    total_clicks = 0
    total_earned = 0

    for row in results:
        title = row[0]
        clicks = row[1]
        earned = row[2] if row[2] else 0.00

        total_clicks += clicks
        total_earned += earned

        stats.append({
            "title": title,
            "clicks": clicks,
            "total": earned
        })

    return render_template("admin.html", stats=stats, total_clicks=total_clicks, total_earned=total_earned)






@app.route('/ad/<int:ad_id>')
def ad_click(ad_id):
    if 'user_id' not in session:
        return redirect('/login')

    user_id = session['user_id']
    ip = request.remote_addr

    cursor = mysql.connection.cursor()
    ClickTracker.register_click(cursor, user_id, ad_id, ip)
    mysql.connection.commit()
    cursor.close()

    # Redirige al link real
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT url FROM ads WHERE id = %s", (ad_id,))
    ad_url = cursor.fetchone()
    cursor.close()

    if ad_url:
        return redirect(ad_url[0])
    else:
        return "Publicidad no encontrada", 404




@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')

if __name__ == '__main__':
    app.run(debug=True)
    
