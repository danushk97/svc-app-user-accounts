CREATE TABLE IF NOT EXISTS public.accounts (
    id SERIAL NOT NULL PRIMARY KEY,
    stable_id uuid NOT NULL UNIQUE DEFAULT uuid_generate_v1(),
    name varchar(128) NOT NULL,
    dob date not null,
    username varchar(50) NOT NULL UNIQUE,
	email varchar(128) NOT NULL UNIQUE,
    phone_number integer UNIQUE,
    is_active boolean DEFAULT true,
    isemail_verified boolean DEFAULT false,
    isphone_number_verified boolean DEFAULT false,
    created_at timestamp without time zone NOT NULL DEFAULT timezone('utc'::text, now()),
    created_by integer,
    last_updated_at timestamp without time zone NOT NULL DEFAULT timezone('utc'::text, now()),
    last_updated_by integer
);

CREATE TABLE IF NOT EXISTS public.passwords (
    id SERIAL NOT NULL PRIMARY KEY,
    username varchar(50) NOT NULL UNIQUE,
    hash bytea NOT NULL,
    is_active boolean DEFAULT true,
    created_at timestamp without time zone NOT NULL DEFAULT timezone('utc'::text, now()),
    created_by integer,
    last_updated_at timestamp without time zone NOT NULL DEFAULT timezone('utc'::text, now()),
    last_updated_by integer,
    FOREIGN KEY (username) REFERENCES public.accounts (username) ON DELETE CASCADE,
    FOREIGN KEY (created_by) REFERENCES public.accounts (id) ON DELETE CASCADE,
    FOREIGN KEY (last_updated_by) REFERENCES public.accounts (id) ON DELETE CASCADE
);
