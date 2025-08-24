# 📊 Predicción de Calificaciones Matemáticas

[![Demo](https://res.cloudinary.com/dguhnftxe/image/upload/v1756027238/devstagram/form_image_rmt24s.png)](https://math-student-grade.onrender.com/)

> **🌐 [¡Prueba la aplicación en vivo!](https://math-student-grade.onrender.com/)**

Una aplicación web moderna que utiliza Machine Learning para predecir calificaciones matemáticas de estudiantes basándose en diversos factores educativos y demográficos.

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.0.3-green.svg)](https://flask.palletsprojects.com/)
[![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.3+-orange.svg)](https://scikit-learn.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Live Demo](https://img.shields.io/badge/Live%20Demo-Online-brightgreen.svg)](https://math-student-grade.onrender.com/)

## 🎯 Descripción del Proyecto

Este proyecto implementa un sistema de **Machine Learning** para predecir calificaciones matemáticas de estudiantes basándose en diversos factores educativos y demográficos. La aplicación utiliza un modelo de **Regresión Lineal** entrenado con datos históricos de rendimiento académico.

### 🌟 Características Principales

- **🤖 Modelo de ML**: Regresión Lineal optimizada para predicciones precisas
- **🌐 Interfaz Web**: Formulario interactivo con diseño moderno y responsivo
- **📱 Diseño Responsivo**: Funciona perfectamente en dispositivos móviles y desktop
- **⚡ API REST**: Endpoint para predicciones en tiempo real
- **🎨 UI Moderna**: Diseño con gradientes, animaciones y efectos glassmorphism

## 🚀 Tecnologías Utilizadas

### Backend
- **Python 3.11+**
- **Flask**: Framework web ligero y flexible
- **Scikit-learn**: Biblioteca de Machine Learning
- **NumPy & Pandas**: Manipulación de datos
- **Joblib**: Serialización del modelo entrenado

### Frontend
- **HTML5**: Estructura semántica
- **CSS3**: Estilos modernos con gradientes y animaciones
- **JavaScript**: Interactividad y validación de formularios
- **Responsive Design**: Adaptable a todos los dispositivos

## 📁 Estructura del Proyecto

```
formulario-educativo/
├── app/
│   ├── __init__.py
│   ├── app.py                 # Aplicación principal Flask
│   ├── models/
│   │   └── lin_reg_model_opt.pkl  # Modelo entrenado
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css      # Estilos modernos
│   │   └── js/
│   │       └── app.js         # JavaScript interactivo
│   └── templates/
│       └── index.html         # Plantilla principal
├── models/
│   └── lin_reg_model_opt.pkl  # Copia del modelo
├── requirements.txt           # Dependencias Python
├── render.yaml               # Configuración para Render
└── README.md                 # Este archivo
```

## 🎯 Variables del Modelo

El modelo utiliza las siguientes variables para realizar predicciones:

| Variable | Tipo | Descripción | Valores |
|----------|------|-------------|---------|
| `gender` | Categórica | Género del estudiante | 0: Femenino, 1: Masculino |
| `lunch` | Categórica | Tipo de almuerzo | 0: Gratuito/Reducido, 1: Estándar |
| `test_preparation_course` | Categórica | Curso de preparación | 0: Ninguno, 1: Completado |
| `reading_score` | Numérica | Puntuación de lectura | 0-100 |
| `writing_score` | Numérica | Puntuación de escritura | 0-100 |
| `race_ethnicity_group_E` | Categórica | Grupo étnico E | 0: No, 1: Sí |
| `parental_level_of_education_high_school` | Categórica | Nivel educativo padres | 0: Otro, 1: Solo Secundaria |

## 🚀 Instalación y Ejecución

### Prerrequisitos
- Python 3.11 o superior
- pip (gestor de paquetes de Python)

### Pasos de Instalación

1. **Clonar el repositorio**
   ```bash
   git clone <url-del-repositorio>
   cd formulario-educativo
   ```

2. **Crear entorno virtual (recomendado)**
   ```bash
   python -m venv venv
   
   # En Windows
   venv\Scripts\activate
   
   # En macOS/Linux
   source venv/bin/activate
   ```

3. **Instalar dependencias**
   ```bash
   pip install -r requirements.txt
   ```

4. **Ejecutar la aplicación**
   ```bash
   python app/app.py
   ```

5. **Abrir en el navegador**
   ```
   http://localhost:5000
   ```

## 🎨 Características del Diseño

### Diseño Moderno
- **Gradientes atractivos**: Fondo con degradado púrpura-azul
- **Glassmorphism**: Efectos de cristal con backdrop-filter
- **Animaciones suaves**: Transiciones y efectos hover
- **Tipografía moderna**: Fuente Inter para mejor legibilidad

### Responsive Design
- **Grid adaptativo**: Se ajusta automáticamente a diferentes pantallas
- **Mobile-first**: Optimizado para dispositivos móviles
- **Breakpoints inteligentes**: Adaptación fluida entre tamaños

### Interactividad
- **Validación en tiempo real**: Verificación de campos requeridos
- **Feedback visual**: Mensajes de éxito y error con iconos
- **Estados de focus**: Indicadores visuales claros
- **Animaciones de carga**: Indicadores de procesamiento

## 🔧 API Endpoints

### POST `/predict`
Realiza una predicción de calificación matemática.

**Request Body (JSON):**
```json
{
  "gender": 0,
  "lunch": 1,
  "test_preparation_course": 0,
  "reading_score": 85.0,
  "writing_score": 82.0,
  "race_ethnicity_group_E": 0,
  "parental_level_of_education_high_school": 1
}
```

**Response:**
```json
{
  "math_score_prediction": 78.5,
  "success": true
}
```

## 🌐 Despliegue

### 🚀 Aplicación en Vivo
**¡Prueba la aplicación ahora mismo!**
- **🔗 URL**: [https://math-student-grade.onrender.com/](https://math-student-grade.onrender.com/)
- **📱 Responsive**: Funciona perfectamente en móviles y desktop
- **⚡ Tiempo real**: Predicciones instantáneas con el modelo de ML

### 🛠️ Despliegue Local
Si quieres ejecutar el proyecto en tu máquina local, sigue las instrucciones de instalación más arriba.

### ☁️ Despliegue en la Nube

#### Render (Recomendado)
El proyecto está configurado para desplegarse en Render:

1. Conecta tu repositorio de GitHub a Render
2. Render detectará automáticamente la configuración en `render.yaml`
3. El despliegue se realizará automáticamente

#### Otros Proveedores
- **Railway**: Compatible con `railway.json`
- **Heroku**: Requiere `Procfile`
- **DigitalOcean App Platform**: Configuración manual

## 📊 Modelo de Machine Learning

### 📚 Dataset y Fuentes de Datos
- **Origen**: [Kaggle - Students Performance in Exams](https://www.kaggle.com/datasets/spscientist/students-performance-in-exams)
- **Tamaño**: 1000 estudiantes
- **Variables**: 8 características (3 numéricas, 5 categóricas)
- **Licencia**: Permite uso comercial y no comercial
- **Calidad**: Datos limpios y bien estructurados

### Algoritmo
- **Regresión Lineal**: Modelo simple pero efectivo para predicciones
- **Optimización**: Hiperparámetros ajustados para mejor rendimiento
- **Validación**: Evaluado con métricas de precisión y R²

### Precisión del Modelo
- **R² Score**: Indica la calidad de las predicciones
- **Validación cruzada**: Robustez del modelo verificada
- **Datos de entrenamiento**: Basado en dataset educativo real

### 📈 Proceso de Entrenamiento

El modelo fue entrenado siguiendo un proceso riguroso y sistemático de análisis de datos:

#### 🔍 **1. Análisis Exploratorio de Datos (EDA)**
- **Dataset**: 1000 estudiantes con 8 variables (3 numéricas, 5 categóricas)
- **Variables originales**: Género, raza/etnia, nivel educativo de padres, tipo de almuerzo, curso de preparación, puntuaciones de matemáticas, lectura y escritura
- **Análisis de correlaciones**: Identificación de relaciones entre variables
- **Distribución de datos**: Estudio de patrones y outliers

#### 🧹 **2. Preprocesamiento de Datos**
- **Limpieza de nombres**: Estandarización de nombres de columnas
- **Encoding de variables categóricas**:
  - **Label Encoding** para variables binarias (género, almuerzo, curso de preparación)
  - **One-Hot Encoding** para variables multiclase (raza/etnia, nivel educativo)
- **Eliminación de multicolinealidad**: Drop de primera categoría en One-Hot Encoding

#### 📊 **3. Feature Engineering**
- **Selección de variables relevantes**: Filtrado por correlación > 0.1 con la variable objetivo
- **Variables finales seleccionadas**:
  - `reading_score` (corr: 0.818) - **Muy alta correlación**
  - `writing_score` (corr: 0.803) - **Muy alta correlación**
  - `lunch` (corr: 0.351) - **Correlación moderada**
  - `race_ethnicity_group_E` (corr: 0.206) - **Correlación baja**
  - `test_preparation_course` (corr: 0.178) - **Correlación baja**
  - `gender` (corr: 0.168) - **Correlación baja**

#### ⚖️ **4. Normalización de Datos**
- **StandardScaler**: Estandarización de todas las variables numéricas
- **Media = 0, Desviación = 1**: Para mejorar la convergencia del modelo
- **Parámetros guardados**: Para aplicar la misma transformación en producción

#### 🤖 **5. Entrenamiento del Modelo**
- **Algoritmo seleccionado**: Regresión Lineal (por la fuerte linealidad observada en los datos)
- **Validación cruzada**: Para evaluar la robustez del modelo
- **Optimización de hiperparámetros**: Ajuste fino del modelo
- **Métricas de evaluación**: R² Score, RMSE, MAE

#### 📈 **6. Resultados y Validación**
- **R² Score**: Indica la calidad de las predicciones
- **Validación en conjunto de prueba**: Evaluación de la generalización
- **Análisis de residuos**: Verificación de supuestos del modelo lineal

> 📖 **Nota**: Puedes revisar el proceso completo de entrenamiento en el archivo `ESTUDIO_DE_DATOS_Predicción_nota_estudiantes.ipynb` y `DS_NL_Regresión_Lineal_Notebook_resumen`

#### 🎯 **Insights Clave del Análisis**
- **Lectura y escritura** son los predictores más fuertes de matemáticas
- **Tipo de almuerzo** tiene una influencia moderada en el rendimiento
- **Variables sociales** tienen menor impacto que las académicas
- **Modelo lineal** es apropiado debido a las fuertes correlaciones lineales observadas

## 🛠️ Desarrollo

### Estructura del Código
- **Modular**: Separación clara entre frontend y backend
- **Mantenible**: Código limpio y bien documentado
- **Escalable**: Fácil agregar nuevas funcionalidades

### Archivos Principales
- `app/app.py`: Lógica principal de Flask
- `app/static/css/style.css`: Estilos modernos
- `app/static/js/app.js`: Interactividad del frontend
- `app/templates/index.html`: Estructura HTML

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Para contribuir:

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📝 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## 👨‍💻 Autor

Desarrollado como proyecto educativo para demostrar la integración de Machine Learning con aplicaciones web modernas.

## 🙏 Agradecimientos

- **Scikit-learn**: Por la biblioteca de Machine Learning
- **Flask**: Por el framework web ligero
- **Comunidad de desarrolladores**: Por las herramientas y recursos

---

⭐ **¡Si te gusta este proyecto, dale una estrella en GitHub!**
