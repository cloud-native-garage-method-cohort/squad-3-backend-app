#!/bin/bash
psql -v ON_ERROR_STOP=1 --username "$DATABASE_USER" -d "$DATABASE_NAME"  <<-EOSQL
     create schema if not exists $SCHEMA;
     create table $SCHEMA.employee (
        id serial PRIMARY KEY,
        firstName VARCHAR ( 50 ) NOT NULL,
        lastName VARCHAR ( 50 ) NOT NULL,
        email VARCHAR ( 255 ) UNIQUE NOT NULL
     );
EOSQL


