# Tener el usuario, el tenant, la contraseña de la base de datos, servidor vps con supabase, y el nombre de 

# Supabase -------------------------------------------------------

#TRABAJAR UNICAMENTE CON EL PERFIL supabase_admin [no hay necesidad de concederle permisos]

# Superset -------------------------------------------------------

# Probar conexion
psql "postgresql://<USUARIO>.<TENANT_ID>:<TU_PASSWORD>@<SERVIDOR>:5432/postgres?sslmode=disable"
