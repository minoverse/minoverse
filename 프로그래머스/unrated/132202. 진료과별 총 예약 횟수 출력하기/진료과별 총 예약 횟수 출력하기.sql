-- 코드를 입력하세요
SELECT
MCDP_CD AS '진료과코드', COUNT('진료과코드') AS '5월예약건수'
FROM
APPOINTMENT
WHERE
APNT_YMD LIKE '_____05%'
GROUP BY
MCDP_CD
ORDER BY 
5월예약건수, 진료과코드;
