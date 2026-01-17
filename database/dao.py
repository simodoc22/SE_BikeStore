from database.DB_connect import DBConnect
from model.category import Category
from model.product import Product

class DAO:
    @staticmethod
    def get_date_range():
        conn = DBConnect.get_connection()

        results = []

        cursor = conn.cursor(dictionary=True)
        query = """ SELECT DISTINCT order_date
                        FROM `order` 
                        ORDER BY order_date """
        cursor.execute(query)

        for row in cursor:
            results.append(row["order_date"])

        first = results[0]
        last = results[-1]

        cursor.close()
        conn.close()
        return first, last

    @staticmethod
    def get_category():
        conn = DBConnect.get_connection()

        results = []

        cursor = conn.cursor(dictionary=True)
        query = """ SELECT * FROM category """
        cursor.execute(query)

        for row in cursor:
            oggetto = Category(row["id"],row["category_name"])
            results.append(oggetto)

        cursor.close()
        conn.close()
        return results


    def get_prodotti(self,categoria):
        conn = DBConnect.get_connection()

        results = set()
        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ SELECT * FROM product """
        cursor.execute(query)

        for row in cursor:
            if row["category_id"]==categoria:
                oggetto = Product(row["id"], row["product_name"],row["category_id"])
                results.add(oggetto)
            else:
                pass

        for i in results:
            result.append(i)

        cursor.close()
        conn.close()
        return result


    def get_order(self,data_inizio,data_fine):
        conn = DBConnect.get_connection()

        results = {}

        cursor = conn.cursor(dictionary=True)
        query = """ SELECT order_date,product_id FROM bike_store_full.order AS ord,bike_store_full.order_item AS ord_i WHERE ord.id = ord_i.order_id """
        cursor.execute(query)

        for row in cursor:
            data_ordine= row["order_date"]
            id_prodotto= row["product_id"]
            if data_inizio<=data_ordine<=data_fine:
                if id_prodotto not in results:
                    results[id_prodotto]= [data_ordine]
                else:
                    results[id_prodotto].append(data_ordine)
            else:
                continue
        cursor.close()
        conn.close()
        return results






