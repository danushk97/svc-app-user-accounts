CREATE TABLE
user_accounts (
	id 		  	 SERIAL PRIMARY KEY,
	stable_id 	 UUID     DEFAULT uuid_generate_v1() NOT NULL,
	attr 		 JSONB 	 					 		 NOT NULL,
	created_date TIMESTAMP WITHOUT TIME ZONE DEFAULT (NOW() AT TIME ZONE 'utc') NOT NULL
);


CREATE TABLE
user_password (
	id           SERIAL PRIMARY KEY,
	stable_id    UUID DEFAULT uuid_generate_v1()  NOT NULL,
    user_id      UUID 							  NOT NULL,
	attr      	 JSONB							  NOT NULL,
	created_date TIMESTAMP WITHOUT TIME ZONE DEFAULT (NOW() AT TIME ZONE 'utc') NOT NULL
)
