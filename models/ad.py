class Advertisement:
    def __init__(self, id, title, url, pay_per_click):
        self.id = id
        self.title = title
        self.url = url
        self.pay_per_click = pay_per_click
        self.description = self.get_description()
        self.image = self.get_image()

    def get_description(self):
        descriptions = {
            1: "Hospeda tu web de forma rápida y segura con SiteGround.",
            2: "Creamos sitios web profesionales y a medida.",
            3: "Explora la tecnología más avanzada en Venezuela."
        }
        return descriptions.get(self.id, "Publicidad")

    def get_image(self):
        images = {
            1: "siteground.jpg",
            2: "josuweb.jpg",
            3: "megatecno.jpg"
        }
        return images.get(self.id, "default.jpg")

    @staticmethod
    def get_all(db_cursor):
        # 🔁 Asegura orden por ID
        db_cursor.execute("SELECT * FROM ads ORDER BY id ASC")
        results = db_cursor.fetchall()
        return [Advertisement(*row) for row in results]
