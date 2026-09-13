# Write your MySQL query statement below
SELECT * 
FROM CINEMA
WHERE DESCRIPTION != 'boring' AND ID%2 = 1
ORDER BY RATING DESC;