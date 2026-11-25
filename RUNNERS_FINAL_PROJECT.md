# Runners - Proyecto Final

## 1. Resumen Ejecutivo
Runners es una plataforma disruptiva de gestión y análisis de eventos de running, diseñada como una réplica inteligente y optimizada de soluciones tradicionales como Kibi. Utiliza IA para transformar la experiencia estática del corredor en una experiencia dinámica, personalizada y altamente compartible.

## 2. Componentes del MVP
- **Interfaz (Frontend):** `index.html`. Dashboard responsivo basado en Tailwind CSS, centrado en la usabilidad del corredor.
- **Motor de Inteligencia (Backend):** `ai_coach.py`. Script en Python que analiza el rendimiento de los corredores y genera feedback inteligente automáticamente.
- **Base de Datos (Sugerida):** Supabase (Gratuito). Sustituye archivos planos por una base de datos relacional escalable.

## 3. Hoja de Ruta para Producción (Costo $0)
1. **Despliegue del Frontend:** Sube `index.html` a [Netlify](https://www.netlify.com/) o [GitHub Pages](https://pages.github.com/). Es gratuito y tarda menos de 5 minutos.
2. **Despliegue del Backend:** Usa [Render](https://render.com/) o [PythonAnywhere](https://www.pythonanywhere.com/) para alojar el script `ai_coach.py` convertido en una pequeña API (Flask).
3. **Automatización:** Conecta el formulario de resultados (Excel/CSV de los organizadores) directamente a Supabase para que el sitio se actualice en tiempo real.

## 4. Diferenciales Estratégicos
- **AI Coach:** Valor añadido gratuito que los atletas aman.
- **Optimización de Costos:** $0 en licencias.
- **Cero fricción:** Interfaz rápida sin necesidad de descargar Apps pesadas.

---
*Diseñado por Claude. 
Proyecto terminado: 24 de noviembre de 2026.*
