-- 코드를 작성해주세요
select count(A.FISH_TYPE) FISH_COUNT, B.FISH_NAME from FISH_INFO A
join FISH_NAME_INFO B on A.FISH_TYPE = B.FISH_TYPE
group by B.FISH_NAME
order by FISH_COUNT desc
