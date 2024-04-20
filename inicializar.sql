INSERT INTO Banco.Departamento (dep_id, nombre, cantidad_poblacion) VALUES
(101, 'Amazonas', 78879),
(102, 'Antioquia', 6737122),
(103, 'Atlantico', 2631905),
(104, 'Bolivar', 2101721),
(105, 'Caldas', 986363),
(106, 'Quindio', 559479),
(107, 'Risaralda', 984605),
(108, 'Santander', 2089738),
(109, 'Tolima', 1408275),
(110, 'Valle del Cauca', 4640617);

INSERT INTO Banco.Prioridad (prd_id, nombre) VALUES
(201, 'Muy importante'),
(202, 'Importante'),
(203, 'Medianamente importante'),
(204, 'Poco importante');

INSERT INTO Banco.Municipio (mun_id, nombre, cantidad_poblacion, dep_id, prd_id) VALUES
(301, 'Leticia', 78879, 101, 203),
(302, 'Medellin', 6737122, 102, 201),
(303, 'Malambo', 274346, 103, 204),
(304, 'Cartagena de Indias', 973045, 104, 202),
(305, 'Manizales', 446160, 107, 202),
(306, 'Armenia', 446160, 106, 203),
(307, 'Quimbaya', 35618, 106, 204);


INSERT INTO Banco.Empleado (emp_id, cedula, nombre, direccion, telefono) VALUES
(401, '1234567890', 'Juan Perez', 'Calle 123', '123456789'),
(402, '987654321', 'María González', 'Carrera 456', '0987654321'),
(403, '1357924680', 'Pedro Ramírez', 'Avenida Principal', '1112223333'),
(404, '2468013579', 'Laura Martínez', 'Calle Secundaria', '1112223333'),
(405, '9876543210', 'Ana López', 'Carrera 789', '1112223333'),
(406, '1111111111', 'Andrés López', 'Carrera 10', '1112223333'),
(407, '2222222222', 'Paola Gómez', 'Calle 20', '1112223333'),
(408, '3333333333', 'Carlos Ramírez', 'Avenida 30', '1112223333'),
(409, '4444444444', 'Ana Martínez', 'Calle 40', '1112223333'),
(410, '5555555555', 'Luisa Pérez', 'Carrera 50', '1112223333'),
(411, '6666666666', 'Juan García', 'Calle 60', '1112223333'),
(412, '7777777777', 'María López', 'Avenida 70', '1112223333'),
(413, '8888888888', 'Pedro González', 'Carrera 80', '1112223333'),
(414, '9999999999', 'Laura Ramírez', 'Calle 90', '1112223333'),
(415, '1010101010', 'Andrea Martínez', 'Avenida 100', '1112223333'),
(416, '1212121212', 'David Pérez', 'Carrera 110', '1112223333'),
(417, '1313131313', 'Carolina García', 'Calle 120', '1112223333'),
(418, '1414141414', 'José Ramírez', 'Avenida 130', '1112223333'),
(419, '1515151515', 'Paula Gómez', 'Carrera 140', '1112223333'),
(420, '1616161616', 'Sofía López', 'Calle 150', '1112223333'),
(421, '1717171717', 'Roberto Martínez', 'Avenida 160', '1112223333'),
(422, '1818181818', 'Elena Pérez', 'Carrera 170', '1112223333'),
(423, '1919191919', 'Daniel García', 'Calle 180', '1112223333'),
(424, '2020202020', 'Valeria Ramírez', 'Avenida 190', '1112223333'),
(425, '2121212121', 'Marcos López', 'Carrera 200', '1112223333');



INSERT INTO Banco.Sucursal (suc_id, nombre, presupuesto_anual, mun_id) VALUES
(501, 'Sucursal Principal', 1000000, 302),
(502, 'Sucursal Central', 1500000, 304),
(503, 'Sucursal Sur', 2000000, 305),
(504, 'Sucursal Este', 2000000, 306);


INSERT INTO Banco.Cargo (carg_id, nombre, salario) VALUES
(601, 'Cajero', 1800000),
(602, 'Asesor', 2200000),
(603, 'Asesor especializado', 2500000),
(604, 'Subdirector', 4500000),
(605, 'Director', 7000000);

INSERT INTO Banco.Funcion (func_id, nombre, descripcion, carg_id) VALUES
(701, 'Funcion1', 'Atender a los clientes en ventanilla', 601),
(702, 'Funcion2', 'Realizar transacciones bancarias, como depósitos y retiros.', 601),
(703, 'Funcion3', 'Gestionar el efectivo en la caja', 601),
(704, 'Funcion4', 'Brindar asesoramiento financiero a los clientes', 602),
(705, 'Funcion5', 'Ayudar a los clientes a elegir productos financieros adecuados para sus necesidades', 602),
(706, 'Funcion6', 'Resolver consultas y problemas de los clientes', 602),
(707, 'Funcion7', 'Brindar asesoramiento experto en áreas específicas, como inversiones, seguros o préstamos hipotecarios', 603),
(708, 'Funcion8', 'Analizar las necesidades financieras de los clientes y recomendar soluciones personalizadas', 603),
(709, 'Funcion9', 'Mantenerse actualizado sobre los cambios en las regulaciones financieras y en los productos del mercado', 603),
(710, 'Funcion10', 'Supervisar las operaciones diarias de la sucursal', 604),
(711, 'Funcion11', 'Apoyar al director en la toma de decisiones estratégicas', 604),
(712, 'Funcion12', 'Coordinar equipos y departamentos para garantizar la eficiencia operativa', 604),
(713, 'Funcion13', 'Establecer objetivos estratégicos para la sucursal y desarrollar planes para alcanzarlos', 605),
(714, 'Funcion14', 'Supervisar todas las actividades y operaciones de la sucursal', 605),
(715, 'Funcion15', 'Representar al banco ante clientes, autoridades reguladoras y otras partes interesadas', 605);






INSERT INTO Banco.Contrato (contr_id, fecha_inicio, fecha_fin, emp_id, suc_id, carg_id) VALUES
(801, '2022-01-01', '2022-12-31', 401, 501, 601),
(802, '2021-10-15', '2022-10-14', 402, 501, 602),
(803, '2022-03-01', '2023-02-28', 403, 501, 603),
(804, '2022-05-20', '2023-05-19', 404, 501, 604),
(805, '2022-02-10', '2023-02-09', 405, 501, 605),
(806, '2022-06-15', '2023-06-14', 406, 501, 602),
(807, '2022-04-20', '2023-04-19', 407, 501, 602),
(808, '2022-08-10', '2023-08-09', 408, 502, 601),
(809, '2022-07-05', '2023-07-04', 409, 502, 602),
(810, '2022-09-25', '2023-09-24', 410, 502, 603),
(811, '2022-11-12', '2023-11-11', 411, 502, 604),
(812, '2022-10-01', '2023-09-30', 412, 502, 605),
(813, '2022-12-20', '2023-12-19', 413, 502, 602),
(814, '2022-08-15', '2023-08-14', 414, 503, 601),
(815, '2022-07-30', '2023-07-29', 415, 503, 602),
(816, '2022-05-05', '2023-05-04', 416, 503, 603),
(817, '2022-03-15', '2023-03-14', 417, 503, 604),
(818, '2022-01-25', '2023-01-24', 418, 503, 605),
(819, '2022-06-01', '2023-05-31', 419, 503, 602),
(820, '2022-04-10', '2023-04-09', 420, 504, 601),
(821, '2022-02-20', '2023-02-19', 421, 504, 602),
(822, '2022-10-15', '2023-10-14', 422, 504, 603),
(823, '2022-11-30', '2023-11-29', 423, 504, 604),
(824, '2022-09-05', '2023-09-04', 424, 504, 605),
(825, '2022-08-20', '2023-08-19', 425, 504, 602);





INSERT INTO `Banco`.`Usuario` (`usr_id`, `nombre_alternativo`, `clave`, `nivel_usuario`)VALUES
    (901, 'escanor', '1999', 'Principal'),
    (902, 'ozzy', '5678', 'Paramétrico'),
    (903, 'gandalf', '8765', 'Esporádico');


INSERT INTO Banco.Profesion (prf_id, nombre) VALUES
(1001, 'Técnico en finanzas'),
(1002, 'Asesor financiero'),
(1003, 'Asesor financiero especializado'),
(1004, 'Administrador de empresas'),
(1005, 'Economista'),
(1006, 'Contador');

INSERT INTO Banco.Detalle_Empleado_Profesion (emp_id, prf_id) VALUES
(401, 1001),
(402, 1002),
(403, 1003),
(404, 1004),
(405, 1005),
(406, 1001),
(407, 1002),
(408, 1003),
(409, 1004),
(410, 1005),
(411, 1001),
(412, 1002),
(413, 1003),
(414, 1004),
(415, 1006),
(416, 1001),
(417, 1002),
(418, 1003),
(419, 1004),
(420, 1005),
(421, 1001),
(422, 1002),
(423, 1003),
(424, 1004),
(425, 1005);



