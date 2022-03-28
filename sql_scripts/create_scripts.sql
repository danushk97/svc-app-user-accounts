CREATE TABLE public.user_accounts
(
    id integer NOT NULL DEFAULT nextval('user_accounts_id_seq'::regclass),
    stable_id uuid NOT NULL DEFAULT uuid_generate_v1(),
    attr jsonb NOT NULL,
    created_date timestamp without time zone NOT NULL DEFAULT timezone('utc'::text, now()),
    CONSTRAINT user_accounts_pkey PRIMARY KEY (id),
    CONSTRAINT unique_stable_id UNIQUE (stable_id)
);

CREATE TABLE public.user_password
(
    id integer NOT NULL DEFAULT nextval('user_password_id_seq'::regclass),
    stable_id uuid NOT NULL DEFAULT uuid_generate_v1(),
    user_id uuid NOT NULL,
    hash bytea NOT NULL,
    created_date timestamp without time zone NOT NULL DEFAULT timezone('utc'::text, now()),
    active_flag boolean DEFAULT false,
    CONSTRAINT user_password_pkey PRIMARY KEY (id),
    CONSTRAINT user_password_user_id_fkey FOREIGN KEY (user_id)
        REFERENCES public.user_accounts (stable_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE CASCADE
);
