create database assessment;
use assessment;

create table customer
(customer_id int,cust_name varchar(50),
city varchar(50),grade int,salesman_id int);

select * from salesman;
insert into customer values
(3002,'nick rimando','new york',100,5001),
(3007,'brad davis','new york',200,5001),
(3005,'Graham zusi','california',200,5002),
(3008,'julian green','london',300,5002),
(3004,'Fabian johnson','paris',300,5006),
(3009,'geoff cameron','berlin',100,5003),
(3003,'jozy altidor','moscow',200,5007),
(3001,'brad guzan','london',null,5001);
CREATE TABLE salesman (salesman_id int,
name varchar(50),city varchar(50),commission float);

insert into salesman values
(5001,'jameshong','newyork',0.15),
(5002,"nail knite",'paris',0.13),
(5005,"pit alex",'london',0.11),
(5006,"mc lyon",'paris',0.14),
(5007,"paul adam",'rome',0.13),
(5003,"lauson hen ","san jose",0.12);

alter table salesman
add primary key(salesman_id);

alter table customer
add foreign key (salesman_id) references salesman(salesman_id);

/*From the above given tables write a SQL query 
to find the salesperson(s) and 
the customer(s) represented here. 
Return the Customer Name, City, 
Salesman, commission.*/

select c.cust_name,c.city,
s.salesman_id,s.commission
from salesman as s
inner join customer as c
on s.salesman_id=c.salesman_id
order by c.cust_name;