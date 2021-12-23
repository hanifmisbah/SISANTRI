import psycopg2
import psycopg2.extras

db = psycopg2.connect(
    host="localhost",
    database="sisantri",
    user="postgres",
    password="hanifmisbah")

cursor = db.cursor()
