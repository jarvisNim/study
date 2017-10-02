create table playground (
	equip_id serial primary key,
	type varchar (50) not null,
	color varchar(25) not null,
	location varchar(25) check (location in ('north','south','west','east')),
	install_data date
);
