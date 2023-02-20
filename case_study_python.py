import configparser

import mysql.connector
from mysql.connector import errorcode

config = {
	"user": "movies_user",
	"password": "popcorn",
	"host": "127.0.0.1",
	"database": "movies",
	"raise_on_warnings": True
}

try:
	db = mysql.connector.connect(**config)
	cursor = db.cursor()

	print("\n Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))

	input("\n\n Press any key to continue...")

	cursor.execute("CREATE TABLE equipment (")
	cursor.execute("equipment_id	INT			NOT NULL	AUTO_INCREMENT,")
	cursor.execute("equipment_amountSold	VARCHAR(75)		NOT NULL,")
	cursor.execute("equipment_amountOnHand	VARCHAR(75)		NOT NULL,")
	cursor.execute("equipment_lastMaintenance	VARCHAR(75)		NOT NULL,")
	cursor.execute("equipment_condition	VARCHAR(75)		NOT NULL,")
	cursor.execute("equipment_nextMaintenance	VARCHAR(75)		NOT NULL,")
	cursor.execute("PRIMARY KEY(equipment_id)")
	cursor.execute(");")

	cursor.execute("CREATE TABLE guides (")
	cursor.execute("guides_id	INT			NOT NULL	AUTO_INCREMENT,")
	cursor.execute("guides_airfareCost	VARCHAR(75)		NOT NULL,")
	cursor.execute("guides_inoculationCount	VARCHAR(75)		NOT NULL,")
	cursor.execute("guides_inventoryCount	VARCHAR(75)		NOT NULL,")
	cursor.execute("guides_inventorySold	VARCHAR(75)		NOT NULL,")
	cursor.execute("guides_supplyCount	VARCHAR(75)		NOT NULL,")
	cursor.execute("PRIMARY KEY(guides_id)")
	cursor.execute(");")

	cursor.execute("CREATE TABLE trip (")
	cursor.execute("trip_id	INT			NOT NULL	AUTO_INCREMENT,")
	cursor.execute("trip_bookingPerYear	VARCHAR(75)		NOT NULL,")
	cursor.execute("trip_locations	VARCHAR(75)		NOT NULL,")
	cursor.execute("trip_costPerPerson	VARCHAR(75)		NOT NULL,")
	cursor.execute("trip_highestBooked	VARCHAR(75)		NOT NULL,")
	cursor.execute("trip_lowestBooked	VARCHAR(75)		NOT NULL,")
	cursor.execute("PRIMARY KEY(trip_id)")
	cursor.execute(");")

	cursor.execute("CREATE TABLE customer (")
	cursor.execute("customer_id	INT			NOT NULL	AUTO_INCREMENT,")
	cursor.execute("customer_fname	VARCHAR(75)		NOT NULL,")
	cursor.execute("customer_lname	VARCHAR(75)		NOT NULL,")
	cursor.execute("customer_age	VARCHAR(75)		NOT NULL,")
	cursor.execute("customer_phoneNumber	VARCHAR(75)		NOT NULL,")
	cursor.execute("customer_equipmentBought	VARCHAR(75)		NOT NULL,")
	cursor.execute("customer_address	VARCHAR(75)		NOT NULL,")
	cursor.execute("customer_rented	VARCHAR(75)		NOT NULL,")
	cursor.execute("equipment_id	INT			NOT NULL,")
	cursor.execute("guides_id	INT			NOT NULL,")
	cursor.execute("trip_id	INT			NOT NULL,")
	cursor.execute("PRIMARY KEY(customer_id)")
	cursor.execute("")
	cursor.execute("CONSTRAINT fk_equipment")
	cursor.execute("FOREIGN KEY(equipment_id)")
	cursor.execute("	REFERENCES equipment(equipment_id),")
	cursor.execute("")
	cursor.execute("CONSTRAINT fk_guides")
	cursor.execute("FOREIGN KEY(guides_id)")
	cursor.execute("	REFERENCES guides(guides_id),")
	cursor.execute("")
	cursor.execute("CONSTRAINT fk_trip")
	cursor.execute("FOREIGN KEY(trip_id)")
	cursor.execute("	REFERENCES trip(trip_id),")
	cursor.execute("")
	cursor.execute(");")

except mysql.connector.Error as err:
	if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
		print(" The supplied username or password are invalid")

	elif err.errno == errorcode.ER_BAD_DB_ERROR:
		print(" The specified database does not exist")

	else:
		print(err)

finally:
	db.close()