# Guía de Uso: Consulta de Acciones y Dividendos (bStocks)

Este instructivo detalla cómo interpretar y utilizar el archivo de referencia `stock_reference_guide.md` para complementar el desarrollo de bots y estrategias de inversión automatizadas dentro de este repositorio (`binance-earn-strategy`).

---

## 1. Conceptos Fundamentales de Dividendos en Acciones

Para operar de forma óptima en torno a la distribución de beneficios, es necesario comprender el ciclo de fechas:

*   **Fecha de Declaración (Declaration Date):** El día en que la junta directiva de la empresa anuncia el monto del dividendo y el calendario oficial.
*   **Fecha Ex-Dividendo (Ex-Dividend Date):** **La fecha más importante para la estrategia.** Es el día de corte en el mercado.
    *   *Si compras antes del Ex-Div:* Recibes el dividendo.
    *   *Si compras en o después del Ex-Div:* No recibes el dividendo; el derecho de cobro se queda con el vendedor anterior.
*   **Fecha de Registro (Record Date):** El día hábil siguiente al ex-dividendo. La empresa verifica quiénes son los accionistas registrados oficialmente.
*   **Fecha de Pago (Payment Date):** El día en que el dinero físico (o los tokens reinvertidos) se depositan en las cuentas de los beneficiarios.

---

## 2. Instrucciones para Usar el Artefacto de Consulta

El archivo de referencia `stock_reference_guide.md` está diseñado como una base de datos estática y rápida de consulta. Debes revisarlo de la siguiente manera:

1.  **Monitorear las Alertas:**
    *   `⚠️ (Hoy / Inminente):` Señala que el activo está cruzando su fecha ex-dividendo en el rango de ±24 horas. Momento crítico para decidir si entrar para capturar el beneficio o esperar el descuento.
    *   `🔔 (Recién Pasado):` Señala que el descuento del dividendo ya se aplicó al precio de mercado (hace menos de 7 días). Excelente oportunidad para acumular acciones ordinarias a un precio "rebajado".
2.  **Validar Estado en Binance:**
    *   Asegúrate de comprobar si la columna *Precio Binance* muestra cotización activa (ej. `TSLABUSDT`). Si dice *No disp.*, significa que el activo solo está disponible a través de la plataforma de corretaje tradicional de Binance y no como un token Spot on-chain (`bStock`).
3.  **Aplicar el Timing Recomendado:**
    *   Sigue las pautas de la columna *Recomendación de Timing* para decidir si tu script debe ejecutar órdenes de compra automáticas o abstenerse temporalmente.

---

## 3. Consideraciones Generales y Precauciones

El trading de acciones y bStocks en el entorno cripto conlleva riesgos particulares que debes considerar:

*   **Retención Fiscal del 30% (Withholding Tax):** Las distribuciones de dividendos de acciones de EE.UU. están sujetas a una retención automática del 30% en origen para inversores extranjeros. Tu bot debe calcular el rendimiento neto basándose en el **70% del dividendo anunciado**, no en el bruto.
*   **Error `-1121` (Invalid Symbol):** Si tu bot intenta consultar o comprar un par como `AAPLBUSDT` y recibe este código de error, se debe a restricciones geográficas aplicadas a tu dirección IP o cuenta (bStocks requiere verificación especial en jurisdicciones aprobadas como la ADGM).
*   **Ausencia de Derechos de Voto:** Los tokens de bStocks son certificados BEP-20; no otorgan derecho de voto en juntas directivas de la empresa emisora. Si tu estrategia requiere gobernanza, debes solicitar la conversión 1:1 a acciones tradicionales en el broker regulado asociado a Binance.
*   **Volatilidad en Fechas Ex-Dividendo:** En la mañana del día ex-dividendo, el precio de la acción caerá de forma automática aproximadamente en la misma magnitud del dividendo. Evita colocar órdenes "Stop Loss" muy ajustadas ese día para prevenir liquidaciones accidentales por el salto de precio (*gap* de apertura).

---

## 4. Prácticas Comunes del Ambiente (Estrategias)

*   **Captura de Dividendos (Dividend Capture):** Comprar el activo 2 o 3 días antes de la fecha ex-dividendo, asegurar el derecho al cobro y vender el activo el día ex-dividendo (después del ajuste de precio) una vez que el mercado comience a recuperar el descuento.
*   **Acumulación por Descuento (Ex-Div Accumulation):** Ignorar el cobro del dividendo y programar compras el mismo día ex-dividendo. Esto te permite acumular más unidades del activo a largo plazo gastando menos USDT.
*   **Arbitraje con Simple Earn:** Cuando las tasas de rendimiento de dividendos anualizados de un bStock son muy superiores a la tasa anualizada (APR) de los ahorros flexibles de Binance Earn, los operadores retiran temporalmente su liquidez de Simple Earn para capturar el dividendo y, tras la fecha de corte, regresan los fondos a Earn.
