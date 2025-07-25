class ClickTracker:
    @staticmethod
    def register_click(db_cursor, user_id, ad_id, ip):
        db_cursor.execute(
            "INSERT INTO clicks (user_id, ad_id, ip_address) VALUES (%s, %s, %s)",
            (user_id, ad_id, ip)
        )
