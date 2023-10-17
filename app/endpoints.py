from sqlalchemy.orm import Session
import h3
from sqlalchemy import text


def get_aggregate_in_radius(db: Session, request):
    lng, lat = request.geometry.coordinates
    origin = h3.geo_to_h3(lat, lng, 11)
    k_ring = h3.k_ring(origin, request.r)
    hex_strings = ["'" + hex + "'" for hex in k_ring]
    hexagon_list = ", ".join(hex_strings)
    raw_sql_query = text(f"""
                    SELECT {request.aggr}(apartments.apartments) 
                    FROM apartments
                    INNER JOIN hex ON apartments.id = hex.id
                    WHERE hex IN ({hexagon_list});
                """)
    result = db.execute(raw_sql_query).fetchone()[0]

    db.close()
    return result


def get_aggregate_in_polyfill(db: Session, request):
    polygon = h3.polyfill(dict(request.geometry), 11, geo_json_conformant=True)
    hex_strings = ["'" + hex + "'" for hex in polygon]
    hexagon_list = ", ".join(hex_strings)

    raw_sql_query = text(f"""
                SELECT {request.aggr}(apartments.price) 
                FROM apartments
                INNER JOIN hex ON apartments.id = hex.id
                WHERE hex IN ({hexagon_list});
            """)
    result = db.execute(raw_sql_query).fetchone()[0]

    db.close()
    return result
