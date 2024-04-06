INSERT INTO `Banco`.`Departamento` (`dep_id`, `nombre`, `cantidad_poblacion`) VALUES
(101, 'Amazonas', 78879),
(102, 'Antioquia', 6737122),
(103, 'Atlántico', 2631905),
(104, 'Bolívar', 2101721),
(105, 'Caldas', 986363),
(106, 'Quindío', 559479),
(107, 'Risaralda', 984605),
(108, 'Santander', 2089738),
(109, 'Tolima', 1408275),
(110, 'Valle del Cauca', 4640617);


INSERT INTO `Banco`.`Usuario` (`usr_id`, `nombre_alternativo`, `clave`, `nivel_usuario`)VALUES
    (201, 'escanor', '1999', 'Principal'),
    (202, 'ozzy', '5678', 'Paramétrico'),
    (203, 'gandalf', '8765', 'Esporádico');



INSERT INTO `Banco`.`Municipio` (`mun_id`, `nombre`, `cantidad_poblacion`, `tipo_municipio`) VALUES
(301, 'Leticia', 78879, 'Medianamente importante'),
(302, 'Medellín', 6737122, 'Muy importante'),
(303, 'Malambo', 274346, 'Poco Importante'),
(304, 'Cartagena de Indias', 973045, 'Importante'),
(305, 'Manizales', 446160, 'Importante'),
(306, 'Armenia', 446160, 'Medianamente importante'),
(307, 'Quimbaya', 35618, 'Poco importante');


INSERT INTO `Banco`.`Cargo` (`carg_id`, `nombre`, `salario`, `funciones`) VALUES
(401, 'Cajero', 1800000, 'Realizar operaciones bancarias, atención al cliente y manejo de efectivo'),
(402, 'Asesor', 2200000, 'Brindar asesoramiento a clientes en productos y servicios financieros'),
(403, 'Asesor especializado', 2500000, 'Brindar asesoramiento especializado en áreas específicas'),
(404, 'Subdirector', 4500000, 'Apoyar al director en la gestión y administración de la organización'),
(405, 'Director', 7000000, 'Dirigir y supervisar todas las actividades de la organización');


INSERT INTO `Banco`.`Sucursal` (`suc_id`, `nombre`, `presupuesto_anual`, `dep_id`, `mun_id`) VALUES
(501, 'Sucursal Principal', 10000000, 102, 302),
(502, 'Sucursal Central', 8000000, 105, 305),
(503, 'Sucursal Norte', 6000000, 101, 301),
(504, 'Sucursal Sur', 7000000, 106, 306),
(505, 'Sucursal Este', 8500000, 107, 307);


INSERT INTO `Banco`.`Empleado` (`emp_id`, `cedula`, `nombre`, `direccion`, `telefono`, `profesion`, `carg_id`, `suc_id`) VALUES
(601, '1234567890', 'Juan Perez', 'Calle 123', '123456789', 'Técnico en finanzas', 401, 501),
(602, '0987654321', 'María González', 'Carrera 456', '987654321', 'Asesor financiero', 402, 501),
(603, '1357924680', 'Pedro Ramírez', 'Avenida Principal', '135792468', 'Asesor financiero especializado', 403, 501),
(604, '2468013579', 'Laura Martínez', 'Calle Secundaria', '246801357', 'Administrador de empresas', 404, 501),
(605, '9876543210', 'Ana López', 'Carrera 789', '9876543210', 'Economista', 405, 501),
(606, '1111111111', 'Andrés López', 'Carrera 10', '111111111', 'Técnico en finanzas', 401, 502),
(607, '2222222222', 'Paola Gómez', 'Calle 20', '222222222', 'Asesor financiero', 402, 502),
(608, '3333333333', 'Carlos Ramírez', 'Avenida 30', '333333333', 'Asesor financiero especializado', 403, 502),
(609, '4444444444', 'Ana Martínez', 'Calle 40', '444444444', 'Administrador de empresas', 404, 502),
(610, '5555555555', 'Luisa Pérez', 'Carrera 50', '555555555', 'Economista', 405, 502),
(611, '6666666666', 'Juan García', 'Calle 60', '666666666', 'Técnico en finanzas', 401, 503),
(612, '7777777777', 'María López', 'Avenida 70', '777777777', 'Asesor financiero', 402, 503),
(613, '8888888888', 'Pedro González', 'Carrera 80', '888888888', 'Asesor financiero especializado', 403, 503),
(614, '9999999999', 'Laura Ramírez', 'Calle 90', '999999999', 'Administrador de empresas', 404, 503),
(615, '1010101010', 'Andrea Martínez', 'Avenida 100', '101010101', 'Economista', 405, 503),
(616, '1212121212', 'David Pérez', 'Carrera 110', '121212121', 'Contador', 401, 504),
(617, '1313131313', 'Carolina García', 'Calle 120', '131313131', 'Asesor financiero', 402, 504),
(618, '1414141414', 'José Ramírez', 'Avenida 130', '141414141', 'Asesor financiero especializado', 403, 504),
(619, '1515151515', 'Paula Gómez', 'Carrera 140', '151515151', 'Administrador de empresas', 404, 504),
(620, '1616161616', 'Sofía López', 'Calle 150', '161616161', 'Economista', 405, 504),
(621, '1717171717', 'Roberto Martínez', 'Avenida 160', '171717171', 'Gerente', 401, 505),
(622, '1818181818', 'Elena Pérez', 'Carrera 170', '181818181', 'Asesor financiero', 402, 505),
(623, '1919191919', 'Daniel García', 'Calle 180', '191919191', 'Asesor financiero especializado', 403, 505),
(624, '2020202020', 'Valeria Ramírez', 'Avenida 190', '202020202', 'Administrador de empresas', 404, 505),
(625, '2121212121', 'Marcos López', 'Carrera 200', '212121212', 'Economista', 405, 505);

INSERT INTO `Banco`.`Contrato` (`contr_id`, `fecha_inicio`, `fecha_fin`, `emp_id`) VALUES
(701, '2022-01-01', '2022-12-31', 601),
(702, '2021-10-15', '2022-10-14', 602),
(703, '2022-03-01', '2023-02-28', 603),
(704, '2022-05-20', '2023-05-19', 604),
(705, '2022-02-10', '2023-02-09', 605),
(706, '2022-06-15', '2023-06-14', 606),
(707, '2022-04-20', '2023-04-19', 607),
(708, '2022-08-10', '2023-08-09', 608),
(709, '2022-07-05', '2023-07-04', 609),
(710, '2022-09-25', '2023-09-24', 610),
(711, '2022-11-12', '2023-11-11', 611),
(712, '2022-10-01', '2023-09-30', 612),
(713, '2022-12-20', '2023-12-19', 613),
(714, '2022-08-15', '2023-08-14', 614),
(715, '2022-07-30', '2023-07-29', 615),
(716, '2022-05-05', '2023-05-04', 616),
(717, '2022-03-15', '2023-03-14', 617),
(718, '2022-01-25', '2023-01-24', 618),
(719, '2022-06-01', '2023-05-31', 619),
(720, '2022-04-10', '2023-04-09', 620),
(721, '2022-02-20', '2023-02-19', 621),
(722, '2022-10-15', '2023-10-14', 622),
(723, '2022-11-30', '2023-11-29', 623),
(724, '2022-09-05', '2023-09-04', 624),
(725, '2022-08-20', '2023-08-19', 625);



