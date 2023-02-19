DROP TABLE IF EXISTS posts;

CREATE TABLE posts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    title TEXT NOT NULL,
    content TEXT NOT NULL
);

CREATE TABLE pcos (
    follicle_r int, 
    follicle_l int, 
    weight_gain int, 
    hair_growth int, 
    skin_darkening int, 
    cycle_r int, 
    fast_food float,  
    pcos int
    );
