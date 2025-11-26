CREATE TABLE IF NOT EXISTS task (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    description TEXT NOT NULL,
    create_date_task TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
    finish_planned_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
    real_finish_date TIMESTAMP DEFAULT NULL,
    create_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
    modificated_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
    create_user VARCHAR(50) DEFAULT CURRENT_USER NOT NULL,
    modificate_user VARCHAR(50) DEFAULT CURRENT_USER NOT NULL
);

CREATE OR REPLACE FUNCTION set_task_dates_and_users() 
RETURNS TRIGGER AS $$
BEGIN
    IF NEW.create_date IS NULL THEN
        NEW.create_date := CURRENT_TIMESTAMP;
    END IF;
    IF NEW.modificated_date IS NULL THEN
        NEW.modificated_date := CURRENT_TIMESTAMP;
    END IF;
    IF NEW.create_user IS NULL THEN
        NEW.create_user := CURRENT_USER;
    END IF;
    IF NEW.modificate_user IS NULL THEN
        NEW.modificate_user := CURRENT_USER;
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER before_insert_task
BEFORE INSERT ON task
FOR EACH ROW
EXECUTE FUNCTION set_task_dates_and_users();

CREATE SEQUENCE task_id_seq START 1;

-- Si decides usar la secuencia manualmente en el campo id, lo harías así:
ALTER TABLE task ALTER COLUMN id SET DEFAULT NEXTVAL('task_id_seq');
