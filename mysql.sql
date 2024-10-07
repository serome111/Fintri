CREATE DATABASE IF NOT EXISTS finanzas;

USE finanzas;

-- Crear la tabla combinada Transacciones
CREATE TABLE IF NOT EXISTS Transacciones (
    id INT AUTO_INCREMENT PRIMARY KEY,
    articulo VARCHAR(255),
    fecha DATE,
    valor DECIMAL(15, 2),
    tipo ENUM('gasto', 'ahorro', 'ingreso'),
    tipo2 VARCHAR(255),
    status TINYINT(1)
);

-- Insertar datos de ingresos en Transacciones
INSERT INTO Transacciones (articulo, fecha, valor, tipo, tipo2) VALUES
('primera quincena', NULL, 5500000.00, 'ingreso', 'IngresosMensuales');

-- Insertar datos de gastos en Transacciones
INSERT INTO Transacciones (articulo, fecha, valor, tipo, tipo2) VALUES
('casa de mamá', NULL, 500000.00, 'gasto', 'GastosMensuales'),
('arriendo y servicios', NULL, 2500000.00, 'gasto', 'GastosMensuales'),
('barbero', NULL, 80000.00, 'gasto', 'GastosMensuales'),
('administración apto', NULL, 50000.00, 'gasto', 'GastosMensuales'),
('gasolina', NULL, 30000.00, 'gasto', 'GastosMensuales'),
('instagram', NULL, 33500.00, 'gasto', 'GastosMensuales'),
('uñas', NULL, 40000.00, 'gasto', 'GastosMensuales'),
('Hbo', NULL, 10000.00, 'gasto', 'GastosMensuales'),
('gasto de algo', NULL, 300000.00, 'gasto', 'GastosMensuales'),
('datos telefono', NULL, 46399.00, 'gasto', 'GastosMensuales'),
('internet', NULL, 77632.00, 'gasto', 'GastosMensuales'),
('Patinio', NULL, 40000.00, 'gasto', 'GastosMensuales');

-- Insertar datos de ahorros en Transacciones
INSERT INTO Transacciones (articulo, fecha, valor, tipo, tipo2) VALUES
('ahorro mensual', '2024-07-15', 500000.00, 'ahorro', 'AhorrosMensuales');
