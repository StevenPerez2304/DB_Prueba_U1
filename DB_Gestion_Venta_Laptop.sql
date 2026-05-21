-- MySQL dump 10.13  Distrib 8.0.45, for Win64 (x86_64)
--
-- Host: localhost    Database: gestion_venta_laptop
-- ------------------------------------------------------
-- Server version	8.0.45

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `cliente`
--

DROP TABLE IF EXISTS `cliente`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cliente` (
  `cedula_cliente` varchar(15) NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `apellido` varchar(50) NOT NULL,
  `direccion` varchar(100) NOT NULL,
  `correo` varchar(100) NOT NULL,
  `telefono` varchar(15) NOT NULL,
  PRIMARY KEY (`cedula_cliente`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cliente`
--

LOCK TABLES `cliente` WRITE;
/*!40000 ALTER TABLE `cliente` DISABLE KEYS */;
INSERT INTO `cliente` VALUES ('0109876543','Pedro','Sanchez','Cuenca','pedro@gmail.com','0983333333'),('0922334455','Lucia','Herrera','Guayaquil','lucia@gmail.com','0984444444'),('1107894561','Juan','Perez','Loja','juan@gmail.com','0981111111'),('1712345678','Ana','Martinez','Quito','ana@gmail.com','0982222222'),('1809988776','Miguel','Castro','Ambato','miguel@gmail.com','0985555555');
/*!40000 ALTER TABLE `cliente` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `credencial`
--

DROP TABLE IF EXISTS `credencial`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `credencial` (
  `cedula_empleado` varchar(15) NOT NULL,
  `correo` varchar(100) NOT NULL,
  `contraseña` varchar(100) NOT NULL,
  PRIMARY KEY (`cedula_empleado`),
  CONSTRAINT `credencial_ibfk_1` FOREIGN KEY (`cedula_empleado`) REFERENCES `empleado` (`cedula_empleado`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `credencial`
--

LOCK TABLES `credencial` WRITE;
/*!40000 ALTER TABLE `credencial` DISABLE KEYS */;
INSERT INTO `credencial` VALUES ('0105874632','luis@empresa.com','12345'),('0923456781','maria@empresa.com','123456'),('1103578942','andrea@empresa.com','1234567'),('1104687291','carlos@empresa.com','123468'),('1804567321','jorge@empresa.com','123456890');
/*!40000 ALTER TABLE `credencial` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `detalle_venta`
--

DROP TABLE IF EXISTS `detalle_venta`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `detalle_venta` (
  `id_detalle_venta` varchar(15) NOT NULL,
  `id_venta` varchar(15) NOT NULL,
  `id_producto` varchar(15) NOT NULL,
  `cantidad` int NOT NULL,
  `precio_unitario` decimal(10,2) NOT NULL,
  `total` decimal(10,2) NOT NULL,
  PRIMARY KEY (`id_detalle_venta`),
  KEY `id_venta` (`id_venta`),
  KEY `id_producto` (`id_producto`),
  CONSTRAINT `detalle_venta_ibfk_1` FOREIGN KEY (`id_venta`) REFERENCES `venta` (`id_venta`),
  CONSTRAINT `detalle_venta_ibfk_2` FOREIGN KEY (`id_producto`) REFERENCES `producto` (`id_producto`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `detalle_venta`
--

LOCK TABLES `detalle_venta` WRITE;
/*!40000 ALTER TABLE `detalle_venta` DISABLE KEYS */;
INSERT INTO `detalle_venta` VALUES ('DET001','VEN001','PROD001',1,750.00,750.00),('DET002','VEN002','PROD002',1,950.00,950.00),('DET003','VEN002','PROD003',1,680.00,680.00),('DET004','VEN003','PROD002',1,950.00,950.00),('DET005','VEN004','PROD001',2,750.00,1500.00),('DET006','VEN005','PROD003',1,680.00,680.00),('DET007','VEN006','PROD004',1,1200.00,1200.00),('DET008','VEN006','PROD001',1,750.00,750.00);
/*!40000 ALTER TABLE `detalle_venta` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `empleado`
--

DROP TABLE IF EXISTS `empleado`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `empleado` (
  `cedula_empleado` varchar(15) NOT NULL,
  `nombre_completo` varchar(100) NOT NULL,
  `apellido_completo` varchar(100) NOT NULL,
  `telefono` varchar(15) NOT NULL,
  `direccion` varchar(100) NOT NULL,
  `cargo` varchar(50) NOT NULL,
  PRIMARY KEY (`cedula_empleado`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `empleado`
--

LOCK TABLES `empleado` WRITE;
/*!40000 ALTER TABLE `empleado` DISABLE KEYS */;
INSERT INTO `empleado` VALUES ('0105874632','Luis','Ramirez','0993333333','Cuenca','Cajero'),('0923456781','Maria','Torres','0994444444','Guayaquil','Supervisor'),('1103578942','Andrea','Lopez','0992222222','Quito','Administrador'),('1104687291','Carlos','Mendoza','0991111111','Loja','Vendedor'),('1804567321','Jorge','Vega','0995555555','Ambato','Vendedor');
/*!40000 ALTER TABLE `empleado` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `factura`
--

DROP TABLE IF EXISTS `factura`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `factura` (
  `numero_factura` varchar(15) NOT NULL,
  `id_venta` varchar(15) NOT NULL,
  `fecha` date NOT NULL,
  `subtotal` decimal(10,2) NOT NULL,
  `IVA` decimal(10,2) NOT NULL,
  `total` decimal(10,2) NOT NULL,
  PRIMARY KEY (`numero_factura`),
  UNIQUE KEY `id_venta` (`id_venta`),
  CONSTRAINT `factura_ibfk_1` FOREIGN KEY (`id_venta`) REFERENCES `venta` (`id_venta`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `factura`
--

LOCK TABLES `factura` WRITE;
/*!40000 ALTER TABLE `factura` DISABLE KEYS */;
INSERT INTO `factura` VALUES ('FAC001','VEN001','2026-05-01',750.00,90.00,840.00),('FAC002','VEN002','2026-05-03',1630.00,195.60,1825.60),('FAC003','VEN003','2026-05-05',950.00,114.00,1064.00),('FAC004','VEN004','2026-05-07',1500.00,180.00,1680.00),('FAC005','VEN005','2026-05-08',680.00,81.60,761.60),('FAC006','VEN006','2026-05-10',1770.00,212.40,1982.40);
/*!40000 ALTER TABLE `factura` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `producto`
--

DROP TABLE IF EXISTS `producto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `producto` (
  `id_producto` varchar(15) NOT NULL,
  `marca` varchar(50) NOT NULL,
  `modelo` varchar(50) NOT NULL,
  `procesador` varchar(50) NOT NULL,
  `ram` varchar(20) NOT NULL,
  `almacenamiento` varchar(20) NOT NULL,
  `tamaño_pantalla` varchar(20) NOT NULL,
  `stock` int NOT NULL,
  `precio` decimal(10,2) NOT NULL,
  PRIMARY KEY (`id_producto`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `producto`
--

LOCK TABLES `producto` WRITE;
/*!40000 ALTER TABLE `producto` DISABLE KEYS */;
INSERT INTO `producto` VALUES ('PROD001','Dell','Inspiron 15','Intel i5','8GB','512GB SSD','15.6',6,750.00),('PROD002','HP','Pavilion','Intel i7','16GB','1TB SSD','14',6,950.00),('PROD003','Lenovo','IdeaPad 3','Ryzen 5','8GB','256GB SSD','15.6',13,680.00),('PROD004','Asus','TUF Gaming','Ryzen 7','16GB','512GB SSD','15.6',4,1200.00),('PROD005','Acer','Aspire 5','Intel i5','12GB','512GB SSD','14',7,820.00);
/*!40000 ALTER TABLE `producto` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `proveedor`
--

DROP TABLE IF EXISTS `proveedor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `proveedor` (
  `ruc` varchar(15) NOT NULL,
  `nombre_empresa` varchar(100) NOT NULL,
  `direccion` varchar(100) NOT NULL,
  `telefono` varchar(15) NOT NULL,
  PRIMARY KEY (`ruc`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `proveedor`
--

LOCK TABLES `proveedor` WRITE;
/*!40000 ALTER TABLE `proveedor` DISABLE KEYS */;
INSERT INTO `proveedor` VALUES ('0198765432001','LaptopWorld','Cuenca','0973333333'),('0991122334001','CompuMarket','Guayaquil','0972222222'),('1199887766001','DigitalStore','Loja','0974444444'),('1790012345001','TechSupplier','Quito','0971111111'),('1899123456001','TecnoImport','Ambato','0975555555');
/*!40000 ALTER TABLE `proveedor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `suministro`
--

DROP TABLE IF EXISTS `suministro`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `suministro` (
  `id_proveedor` varchar(15) NOT NULL,
  `id_producto` varchar(15) NOT NULL,
  `cantidad` int NOT NULL,
  `precio_compra` decimal(10,2) NOT NULL,
  `fecha_suministro` date NOT NULL,
  PRIMARY KEY (`id_proveedor`,`id_producto`),
  KEY `id_producto` (`id_producto`),
  CONSTRAINT `suministro_ibfk_1` FOREIGN KEY (`id_proveedor`) REFERENCES `proveedor` (`ruc`),
  CONSTRAINT `suministro_ibfk_2` FOREIGN KEY (`id_producto`) REFERENCES `producto` (`id_producto`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `suministro`
--

LOCK TABLES `suministro` WRITE;
/*!40000 ALTER TABLE `suministro` DISABLE KEYS */;
INSERT INTO `suministro` VALUES ('0198765432001','PROD003',25,500.00,'2026-04-22'),('0991122334001','PROD002',15,780.00,'2026-04-21'),('1199887766001','PROD004',10,950.00,'2026-04-23'),('1790012345001','PROD001',20,600.00,'2026-04-20'),('1899123456001','PROD005',18,650.00,'2026-04-24');
/*!40000 ALTER TABLE `suministro` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `venta`
--

DROP TABLE IF EXISTS `venta`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `venta` (
  `id_venta` varchar(15) NOT NULL,
  `id_cliente` varchar(15) NOT NULL,
  `id_empleado` varchar(15) NOT NULL,
  `fecha` date NOT NULL,
  PRIMARY KEY (`id_venta`),
  KEY `id_cliente` (`id_cliente`),
  KEY `id_empleado` (`id_empleado`),
  CONSTRAINT `venta_ibfk_1` FOREIGN KEY (`id_cliente`) REFERENCES `cliente` (`cedula_cliente`),
  CONSTRAINT `venta_ibfk_2` FOREIGN KEY (`id_empleado`) REFERENCES `empleado` (`cedula_empleado`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `venta`
--

LOCK TABLES `venta` WRITE;
/*!40000 ALTER TABLE `venta` DISABLE KEYS */;
INSERT INTO `venta` VALUES ('VEN001','1107894561','1104687291','2026-05-01'),('VEN002','1107894561','1103578942','2026-05-03'),('VEN003','1107894561','0105874632','2026-05-05'),('VEN004','1712345678','1104687291','2026-05-07'),('VEN005','1712345678','0923456781','2026-05-08'),('VEN006','0109876543','1804567321','2026-05-10');
/*!40000 ALTER TABLE `venta` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-05-21 18:49:05
