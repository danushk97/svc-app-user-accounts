CREATE TABLE public.users
(
    id SERIAL NOT NULL PRIMARY KEY,
    stable_id uuid NOT NULL UNIQUE DEFAULT uuid_generate_v1(),
    attr jsonb NOT NULL,
    active_flag boolean DEFAULT false,
    isemail_verified boolean DEFAULT false,
    isphone_number_verified boolean DEFAULT false,
    created_at timestamp without time zone NOT NULL DEFAULT timezone('utc'::text, now()),
    created_by uuid,
    updated_at timestamp without time zone NOT NULL DEFAULT timezone('utc'::text, now()),
    updated_by uuid
);

CREATE TABLE public.passwords
(
    id SERIAL NOT NULL PRIMARY KEY,
    stable_id uuid NOT NULL UNIQUE DEFAULT uuid_generate_v1(),
    user_id uuid NOT NULL,
    hash bytea NOT NULL,
    active_flag boolean DEFAULT true,
    created_at timestamp without time zone NOT NULL DEFAULT timezone('utc'::text, now()),
    created_by uuid,
    updated_at timestamp without time zone NOT NULL DEFAULT timezone('utc'::text, now()),
    updated_by uuid,
    CONSTRAINT users_passwords_fkey FOREIGN KEY (user_id)
        REFERENCES public.users (stable_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE CASCADE
);
