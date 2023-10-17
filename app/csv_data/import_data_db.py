import csv
import psycopg2

conn = psycopg2.connect(
    host="db",
    database="admin",
    user="admin",
    password="admin"
)
cursor = conn.cursor()

with open('apartments.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        geo_point = eval(row['geopos'])['coordinates']
        longitude, latitude = geo_point
        apartments = int(row['apartments'])
        price = float(row['price'])
        year = int(row['year'])

        insert_query = "INSERT INTO apartments (geopos, apartments, price, year) VALUES (ST_GeomFromText(%s), %s, %s, %s)"
        cursor.execute(insert_query, (f'POINT({longitude} {latitude})', apartments, price, year))
        conn.commit()

create_add_data_to_hex_id = f"""
            INSERT INTO hex (hex)
            SELECT h3_lat_lng_to_cell(Point(ST_X(ST_GeomFromWKB(geopos)), ST_Y(ST_GeomFromWKB(geopos))), 11)
            FROM apartments;
        """

cursor.execute(create_add_data_to_hex_id)
conn.commit()


cursor.close()
conn.close()
