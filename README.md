# begemotic

Запускаем
```
docker-compose up --build
```

Во втором терминале импортируем данные из csv таблички в нашу бд (ТОЛЬКО ОДИН РАЗ!)
```
docker exec -it fastapi /bin/bash
cd csv_data
python import_data_db.py
```

Шлем запросы на наши эндпоинты 
```
curl -X POST -H "Content-Type: application/json" -d '{
 "geometry": {
   "type": "Point",
   "coordinates": [37.517259, 55.542444]
 },
 "field": "apartments",
 "aggr": "sum",
 "r": 4
}' http://localhost:8000/aggregate_in_radius
```

и
```
curl -X POST -H "Content-Type: application/json" -d '{
 "geometry": {
   "type": "Polygon",
   "coordinates": [[
     [37.520123, 55.54413],
     [37.515671, 55.54399],
     [37.514662, 55.541793],
     [37.521218, 55.542612],
     [37.520123, 55.54413]
   ]]
 },
 "field": "price",
 "aggr": "avg"
}' http://localhost:8000/aggregate_in_polyfill
```
