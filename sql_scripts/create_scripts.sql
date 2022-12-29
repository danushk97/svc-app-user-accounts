CREATE TABLE IF NOT EXISTS public.accounts (
    id SERIAL NOT NULL PRIMARY KEY,
    stable_id uuid NOT NULL UNIQUE DEFAULT uuid_generate_v1(),
    username varchar(50) NOT NULL UNIQUE,
	email varchar(128) NOT NULL UNIQUE,
    attr jsonb NOT NULL,
    active_flag boolean DEFAULT false,
    isemail_verified boolean DEFAULT false,
    isphone_number_verified boolean DEFAULT false,
    created_at timestamp without time zone NOT NULL DEFAULT timezone('utc'::text, now()),
    created_by uuid,
    updated_at timestamp without time zone NOT NULL DEFAULT timezone('utc'::text, now()),
    updated_by uuid
);

CREATE TABLE IF NOT EXISTS public.passwords (
    id SERIAL NOT NULL PRIMARY KEY,
    username varchar(50) NOT NULL UNIQUE,
    hash bytea NOT NULL,
    created_at timestamp without time zone NOT NULL DEFAULT timezone('utc'::text, now()),
    created_by uuid,
    updated_at timestamp without time zone NOT NULL DEFAULT timezone('utc'::text, now()),
    updated_by uuid,
    FOREIGN KEY (username) REFERENCES public.accounts (username) ON DELETE CASCADE,
    FOREIGN KEY (created_by) REFERENCES public.accounts (stable_id) ON DELETE CASCADE,
    FOREIGN KEY (updated_by) REFERENCES public.accounts (stable_id) ON DELETE CASCADE
);
