Project Spec: voxFinance API (Modular Monolith)
1. Visión General

API de procesamiento de resúmenes bancarios que utiliza LLMs de ventana grande y Polars para transformar documentos PDF en informes estratégicos de salud financiera en formato Markdown y PDF.

2. Objetivos Principales

    Validación Inteligente: Filtrar documentos no bancarios mediante análisis de contexto.

    Extracción de Alta Fidelidad: Capturar tablas complejas sin pérdida de datos.

    Análisis Predictivo: Identificar patrones de gasto, anomalías e "insights" financieros.

    Privacidad Efímera: Procesar datos sin persistir el contenido sensible del PDF, solo el reporte final.

3. Arquitectura y Stack

Arquitectura: Monolito Modular (Organizado por dominios: auth, banking, analysis, reports).
Capa,Tecnología
Framework API,"FastAPI (Async, Pydantic v2)"
Base de Datos,PostgreSQL + SQLAlchemy + Alembic
Procesamiento de Datos,Polars (Estructuras tabulares de alto rendimiento)
Extracción PDF,PyMuPDF (Metadatos) + pdfplumber (Tablas)
Cerebro AI,LangChain + LLM (Modelos de ventana de 128k+ tokens)
Reportes,Markdown + WeasyPrint (PDF)

4. Flujo Lógico del Sistema

    Ingesta: Recepción de PDF vía multipart/form-data.

    Gatekeeper (LLM): Envío de las primeras páginas al LLM para confirmar autenticidad bancaria.

    Extracción de Datos: Parseo de tablas con pdfplumber y limpieza con Polars.

    Consolidación: Agregación de transacciones si el resumen es anual.

    Análisis (LLM): Envío de la data estructurada al LLM con el System Prompt de categorías e insights.

    Entrega: Generación de Markdown y conversión opcional a PDF.

5. Alcance del Análisis (Insights)

El sistema debe categorizar y reportar obligatoriamente sobre:

    Categorías: Vivienda, Alimentación, Transporte, Ocio, Salud, Finanzas, Otros.

    Gastos Hormiga: Detección de micro-pagos recurrentes.

    Detección de Anomalías: Gastos fuera del promedio mensual histórico.

    Ratio de Ahorro: Cálculo de capacidad de ahorro mensual.

    Proyección: Estimación de flujo de caja para el mes siguiente.

6. Módulos del Sistema

    auth: Registro, Login y seguridad JWT.

    banking: Lógica de extracción (PyMuPDF/pdfplumber) y validación de documentos.

    analysis: Orquestación de Polars para limpieza y comunicación con LangChain.

    reports: Manejo de plantillas Markdown y generación de archivos de salida.

    shared: Modelos de base de datos base, excepciones personalizadas y utilidades de configuración.