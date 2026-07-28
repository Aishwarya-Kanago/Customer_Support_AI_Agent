from app.database.connection import get_connection


class OrderRepository:

    def get_order(self, order_id: int):

        conn = get_connection()

        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT *
            FROM orders
            WHERE order_id=?
            """,
            (order_id,),
        )

        row = cursor.fetchone()

        conn.close()

        if row is None:
            return None

        return dict(row)


    def get_order_status(self, order_id: int):

        conn = get_connection()

        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT status
            FROM orders
            WHERE order_id=?
            """,
            (order_id,),
        )

        row = cursor.fetchone()

        conn.close()

        if row is None:
            return None

        return row["status"]


    def get_tracking_number(self, order_id: int):

        conn = get_connection()

        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT tracking_number
            FROM orders
            WHERE order_id=?
            """,
            (order_id,),
        )

        row = cursor.fetchone()

        conn.close()

        if row is None:
            return None

        return row["tracking_number"]


    def list_customer_orders(self, customer_name: str):

        conn = get_connection()

        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT *
            FROM orders
            WHERE customer_name=?
            """,
            (customer_name,),
        )

        rows = cursor.fetchall()

        conn.close()

        return [dict(row) for row in rows]