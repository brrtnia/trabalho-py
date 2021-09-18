CREATE TABLE public.register
(
    emailid character varying COLLATE pg_catalog."default" NOT NULL,
    id integer NOT NULL DEFAULT nextval('register_id_seq'::regclass),
    password character varying(30) COLLATE pg_catalog."default" NOT NULL,
    firsthame character varying COLLATE pg_catalog."default" NOT NULL,
    lastname character varying COLLATE pg_catalog."default" NOT NULL,
    username character varying COLLATE pg_catalog."default" NOT NULL,
    birthday character varying(11) COLLATE pg_catalog, "default" NOT NULL,
    gender character varying COLLATE pg_catalog, "default" NOT NULL,
    email character varying(30) COLLATE pg_catalog, "default" NOT NULL,
    CONSTRAINT register_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE public.register
    OWNER to postgres;

CREATE TABLE public.vit_derr
(
    -- Inherited from table public.register: emailid character varying COLLATE pg_catalog."default" NOT NULL,
    -- Inherited from table public.register: id integer NOT NULL DEFAULT nextval('register_id_seq'::regclass),
    -- Inherited from table public.register: password character varying(30) COLLATE pg_catalog."default" NOT NULL,
    -- Inherited from table public.register: username character varying COLLATE pg_catalog."default" NOT NULL,
    -- Inherited from table public.register: "confirm password" character varying(30) COLLATE pg_catalog."default" NOT NULL,
    id_user integer NOT NULL DEFAULT nextval('vit_derr_id_user_seq'::regclass),
    "num_vitórias" integer,
    num_derrotas integer,
    CONSTRAINT vit_derr_pkey PRIMARY KEY (id_user)
)
    INHERITS (public.register)
TABLESPACE pg_default;

ALTER TABLE public.vit_derr
    OWNER to postgres;
