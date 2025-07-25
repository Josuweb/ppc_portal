# main.py (lógica de flujo)
from models.user import User
from models.ad import Advertisement
from models.click import ClickTracker

# Crear usuario
user = User(user_id=1, email="usuario@example.com")
if user.authenticate():
    print("✔ Usuario autenticado correctamente.")

    # Mostrar anuncio
    ad = Advertisement(ad_id=1, title="Compra Ya!", url="https://anuncio.com", pay_per_click=0.10)
    print(ad.display())

    # Simular clic
    tracker = ClickTracker()
    tracker.register_click(user, ad)
else:
    print("❌ Autenticación fallida.")
