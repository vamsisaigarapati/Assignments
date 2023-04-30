select count(*) from yellow_taxi_tripss;

select avg(trip_distance) from yellow_taxi_tripss;

select sum(fare_amount) from yellow_taxi_tripss;
 
													
select locc.borough as borough ,avg(tripp.fare_amount) as average_fare_for_toll_routes from yellow_taxi_tripss tripp join taxilookupp locc on tripp.PULocationID=locc.LocationID where 
tripp.tolls_amount<>0 group by borough;
