/*
a) The information included in this table is the actor_id, their
first_name, last_name, and the last_update. 
b) In this table, the information included is film_id, the title 
and description of the film, its release_year, language_id, length,
original_language, rental_duration, rental_rate, replacement,
rating, special_feattures, and any updates that was made. 
c) The tables film_actor also contains columns for both actor_id
and film_id.
d)This table includes a list of customers ID, rentals ID, and dates. Essentially, it shows which
customers returned what movie by x date. In my opinion, this information is slightly hard to read
because it is just numbers, but other than that, it is not that hard to read. If you take your
time to read each record, it is fairly simple to read and understand.
e)This table includes the store id, film id, the rental id, and when it was last updated. 
This is even easier to read than the rental table. 
f) the tables that I need to understand the names of the films that 
were rented on a specific date are film_id, rental_id and rental_date. These tables
are related to each other because they tell the user who rented what and on
what day. These tables are share the same columns which connects
them to each other.
*/

SELECT film_id FROM film;
SELECT rental_id FROM rental;
SELECT rental_date FROM rental;