Select USERID,OCCUPATION
from Viewer;


Select distinct MOVIETITLE as "Happily Scared"
from Movie 
where HORROR=1 or COMEDY=1;


Select USERID
from Viewer
where Gender = 'M' or
(Occupation = 'student' and Age > 30);


Select distinct Occupation 
from Viewer
where Occupation Not in ('student','lawyer','educator')
order by Occupation desc;


Select MOVIETITLE 
from Movie
where Movietitle like '%(1982)'
order by MOVIETITLE asc;


SELECT VIEWER.UserID, AVG(Rating) 
FROM VIEWER INNER JOIN RATING 
ON VIEWER.UserID = RATING.UserID
GROUP BY VIEWER.UserID
HAVING AVG(Rating) < 2;


Select distinct Max(AGE),occupation
from VIEWER
group by Occupation;


SELECT Occupation, COUNT(1) 
AS "Number of Reviewers" 
FROM VIEWER
GROUP BY Occupation
HAVING Occupation NOT IN ('student','educator');


Select Gender, round(avg(Age),3) 
AS "average age" 
from VIEWER
Group by Gender, Occupation
Having Occupation = 'student';


Select Distinct Occupation 
From VIEWER
Group by Occupation, Gender, Age
Having Gender = 'F'
and avg(Age) > 40;