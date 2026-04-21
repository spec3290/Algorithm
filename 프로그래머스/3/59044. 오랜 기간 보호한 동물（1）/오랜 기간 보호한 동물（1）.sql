-- 코드를 입력하세요
SELECT A.NAME, A.DATETIME from ANIMAL_INS A
left join ANIMAL_OUTS B on A.ANIMAL_ID = B.ANIMAL_ID
where B.NAME is null and A.name is not null
order by A.DATETIME
limit 3
-- WHERE A.NAME in (select NAME FROM ANIMAL_INS
-- order by DATETIME
-- limit 3)