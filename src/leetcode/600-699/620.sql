select
  *
from
  Cinema
where
  description not like '%boring%'
  and mod(id, 2) = 1
order by
  rating desc