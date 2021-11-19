#!/bin/bash
psql -v ON_ERROR_STOP=1 --username "$DATABASE_USER" -d "$DATABASE_NAME"  <<-EOSQL
    INSERT INTO $SCHEMA.employee (firstName, lastName, email)  VALUES ( 'Frank', 'Murphy', 'frank.murphy@test.com');
    INSERT INTO $SCHEMA.employee (firstName, lastName, email)  VALUES ( 'Vic', 'Reynolds', 'vic.reynolds@gmail.com');
    INSERT INTO $SCHEMA.employee (firstName, lastName, email)  VALUES ( 'Gina','Jabowski', 'gina.jabowski@test.com');
    INSERT INTO $SCHEMA.employee (firstName, lastName, email)  VALUES ( 'Jessi', 'Glaser', 'jessi.glaser@yahoo.com');
    INSERT INTO $SCHEMA.employee (firstName, lastName, email)  VALUES ( 'Jay', 'Blizerian', 'jay.bilzerian@test.com');
EOSQL

