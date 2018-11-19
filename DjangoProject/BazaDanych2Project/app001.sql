BEGIN;
--
-- Create model Assortment
--
CREATE TABLE "Projekt_assortment" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "amount" integer NOT NULL, "price" real NOT NULL);
--
-- Create model Books
--
CREATE TABLE "Projekt_books" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "ISBN" integer NOT NULL UNIQUE, "title" varchar(250) NOT NULL, "author" varchar(250) NOT NULL, "publishing_house" varchar(250) NOT NULL, "genre" varchar(250) NOT NULL, "cover" varchar(250) NULL);
--
-- Create model Cart
--
CREATE TABLE "Projekt_cart" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "amount" integer NOT NULL, "assortment_id" integer NOT NULL REFERENCES "Projekt_assortment" ("id") DEFERRABLE INITIALLY DEFERRED);
--
-- Create model CompletedCart
--
CREATE TABLE "Projekt_completedcart" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "amount" integer NOT NULL, "assortment_id" integer NOT NULL REFERENCES "Projekt_assortment" ("id") DEFERRABLE INITIALLY DEFERRED);
--
-- Create model Customer
--
CREATE TABLE "Projekt_customer" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "first_name" varchar(250) NOT NULL, "last_name" varchar(250) NOT NULL, "email" varchar(250) NOT NULL, "tel_number" varchar(250) NOT NULL, "loyalty_card" bool NOT NULL);
--
-- Create model JobTitle
--
CREATE TABLE "Projekt_jobtitle" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "job_title" varchar(250) NOT NULL);
--
-- Create model Order
--
CREATE TABLE "Projekt_order" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "order_date" date NOT NULL, "was_paid" bool NOT NULL, "cash_on_delivery" bool NOT NULL, "was_ordered" bool NOT NULL, "total_amount" real NOT NULL, "completed_order_id" integer NOT NULL REFERENCES "Projekt_completedcart" ("id") DEFERRABLE INITIALLY DEFERRED);
--
-- Create model Worker
--
CREATE TABLE "Projekt_worker" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "first_name" varchar(250) NOT NULL, "last_name" varchar(250) NOT NULL, "email" varchar(250) NOT NULL, "tel_number" varchar(250) NOT NULL, "salary" integer NOT NULL, "job_title_id" integer NOT NULL REFERENCES "Projekt_jobtitle" ("id") DEFERRABLE INITIALLY DEFERRED);
--
-- Add field customer to completedcart
--
ALTER TABLE "Projekt_completedcart" RENAME TO "Projekt_completedcart__old";
CREATE TABLE "Projekt_completedcart" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "amount" integer NOT NULL, "assortment_id" integer NOT NULL REFERENCES "Projekt_assortment" ("id") DEFERRABLE INITIALLY DEFERRED, "customer_id" integer NOT NULL REFERENCES "Projekt_customer" ("id") DEFERRABLE INITIALLY DEFERRED);
INSERT INTO "Projekt_completedcart" ("id", "amount", "assortment_id", "customer_id") SELECT "id", "amount", "assortment_id", NULL FROM "Projekt_completedcart__old";
DROP TABLE "Projekt_completedcart__old";
CREATE INDEX "Projekt_cart_assortment_id_09a2923e" ON "Projekt_cart" ("assortment_id");
CREATE INDEX "Projekt_order_completed_order_id_bd79d53e" ON "Projekt_order" ("completed_order_id");
CREATE INDEX "Projekt_worker_job_title_id_b790b765" ON "Projekt_worker" ("job_title_id");
CREATE INDEX "Projekt_completedcart_assortment_id_b645c5f6" ON "Projekt_completedcart" ("assortment_id");
CREATE INDEX "Projekt_completedcart_customer_id_5ed49b61" ON "Projekt_completedcart" ("customer_id");
--
-- Add field customer to cart
--
ALTER TABLE "Projekt_cart" RENAME TO "Projekt_cart__old";
CREATE TABLE "Projekt_cart" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "amount" integer NOT NULL, "assortment_id" integer NOT NULL REFERENCES "Projekt_assortment" ("id") DEFERRABLE INITIALLY DEFERRED, "customer_id" integer NOT NULL REFERENCES "Projekt_customer" ("id") DEFERRABLE INITIALLY DEFERRED);
INSERT INTO "Projekt_cart" ("id", "amount", "assortment_id", "customer_id") SELECT "id", "amount", "assortment_id", NULL FROM "Projekt_cart__old";
DROP TABLE "Projekt_cart__old";
CREATE INDEX "Projekt_cart_assortment_id_09a2923e" ON "Projekt_cart" ("assortment_id");
CREATE INDEX "Projekt_cart_customer_id_6e792234" ON "Projekt_cart" ("customer_id");
--
-- Add field book to assortment
--
ALTER TABLE "Projekt_assortment" RENAME TO "Projekt_assortment__old";
CREATE TABLE "Projekt_assortment" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "amount" integer NOT NULL, "price" real NOT NULL, "book_id" integer NOT NULL REFERENCES "Projekt_books" ("id") DEFERRABLE INITIALLY DEFERRED);
INSERT INTO "Projekt_assortment" ("id", "amount", "price", "book_id") SELECT "id", "amount", "price", NULL FROM "Projekt_assortment__old";
DROP TABLE "Projekt_assortment__old";
CREATE INDEX "Projekt_assortment_book_id_31bef4c4" ON "Projekt_assortment" ("book_id");
COMMIT;
