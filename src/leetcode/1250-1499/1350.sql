select
  Students.id, Students.name
from
  Students left join Departments on Students.department_id = Departments.id
where
  Departments.id is null