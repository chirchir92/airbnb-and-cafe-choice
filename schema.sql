-- drop table listing;

create table listing (
    id serial primary key,
    host_id int,
    airbnb_name varchar(200),
    host_location varchar(200),
    review_scores_location dec,
    latitude dec(10,5),
    longitude dec(10,5),
    price varchar
    );

-----------------------------------------
-- drop table reviews;

create table reviews (
    id serial primary key,
    listing_id int,
    comments varchar
);

----------------------------------------
-- drop table cafes;

create table cafes (
    id serial primary key,
    airbnb_name varchar,
    latitude dec(10,5),
    longitude dec(10,5),
    cafe_name varchar,
    cafe_rating dec
);