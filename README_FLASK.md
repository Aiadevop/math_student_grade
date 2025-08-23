# 📊 Predicción de Calificaciones Matemáticas - Versión Flask

Esta es la versión Flask de la aplicación de predicción de calificaciones matemáticas, diseñada para funcionar correctamente en Vercel.

## 🚀 Características

- **Modelo de Machine Learning**: Utiliza el modelo `lin_reg_model_opt.pkl` para predicciones
- **API REST**: Endpoints para validación y predicción
- **Interfaz Web**: Formulario HTML integrado con diseño moderno
- **Validación de Datos**: Verificación automática de variables requeridas
- **Compatibilidad con Vercel**: Configurado para despliegue en Vercel

## 📁 Estructura del Proyecto

```
formulario-educativo/
├── app.py                 # Aplicación Flask principal
├── wsgi.py               # Archivo WSGI para servidores
├── requirements_flask.txt # Dependencias de Python
├── vercel.json           # Configuración de Vercel
├── models/               # Carpeta de modelos
│   └── lin_reg_model_opt.pkl # Modelo de Machine Learning
└── README_FLASK.md       # Este archivo
```

## 🔧 Instalación Local

1. **Instalar dependencias**:
   ```bash
   pip install -r requirements_flask.txt
   ```

2. **Ejecutar la aplicación**:
   ```bash
   python app.py
   ```

3. **Acceder a la aplicación**:
   - Abrir http://localhost:5000 en tu navegador

## 🌐 Endpoints de la API

### 1. Página Principal
- **URL**: `/`
- **Método**: GET
- **Descripción**: Formulario HTML para ingresar datos

### 2. Validación de Datos
- **URL**: `/api/escalar`
- **Método**: POST
- **Descripción**: Valida y prepara los datos del formulario

### 3. Predicción
- **URL**: `/api/predict` o `/predict`
- **Método**: POST
- **Descripción**: Realiza predicciones usando el modelo

### 4. Verificación de Salud
- **URL**: `/health`
- **Método**: GET
- **Descripción**: Verifica el estado del servidor y modelo

## 📊 Variables del Modelo

El modelo requiere las siguientes variables (en orden):

1. `gender` - Género (0: Femenino, 1: Masculino)
2. `lunch` - Tipo de almuerzo (0: Gratuito/Reducido, 1: Estándar)
3. `test_preparation_course` - Preparación del examen (0: Ninguna, 1: Completado)
4. `reading_score` - Calificación de lectura (0-100)
5. `writing_score` - Calificación de escritura (0-100)
6. `race_ethnicity_group_E` - Grupo étnico E (0: No, 1: Sí)
7. `parental_level_of_education_high_school` - Nivel educativo de los padres (0: Otro, 1: Secundaria)

## 🚀 Despliegue en Vercel

1. **Subir archivos a GitHub**:
   - Asegúrate de que `lin_reg_model_opt.pkl` esté en la carpeta `models/`
   - Incluye todos los archivos de configuración

2. **Conectar con Vercel**:
   - Importa el repositorio en Vercel
   - Vercel detectará automáticamente la configuración de Python

3. **Variables de entorno** (opcional):
   - No se requieren variables de entorno adicionales

## 🔍 Ejemplo de Uso

### Usando la interfaz web:
1. Abrir la aplicación en el navegador
2. Completar el formulario con los datos del estudiante
3. Hacer clic en "Predecir Calificación Matemática"
4. Ver el resultado de la predicción

### Usando la API directamente:
```bash
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{
    "gender": 1,
    "lunch": 1,
    "test_preparation_course": 1,
    "reading_score": 85.5,
    "writing_score": 82.3,
    "race_ethnicity_group_E": 0,
    "parental_level_of_education_high_school": 1
  }'
```

## 📈 Precisión del Modelo

- **R² Score**: 0.872151 (87.2% de precisión)
- **Tipo de Modelo**: Regresión Lineal Optimizada
- **Validación**: Cross-validation

## 🛠️ Solución de Problemas

### Error: "Modelo no disponible"
- Verifica que `lin_reg_model_opt.pkl` esté en la carpeta `models/`
- Asegúrate de que el archivo no esté corrupto

### Error: "Variable faltante"
- Verifica que todas las variables requeridas estén presentes
- Asegúrate de que los valores sean numéricos

### Error de despliegue en Vercel
- Verifica que `vercel.json` esté configurado correctamente
- Asegúrate de que todas las dependencias estén en `requirements_flask.txt`

## 🔄 Migración desde Next.js

Esta versión Flask reemplaza completamente la funcionalidad de Next.js:

- ✅ **API Routes**: Convertidas a endpoints Flask
- ✅ **Validación**: Mantiene la misma lógica de validación
- ✅ **Modelo**: Utiliza el mismo modelo `lin_reg_model_opt.pkl`
- ✅ **Interfaz**: Formulario HTML integrado con Tailwind CSS
- ✅ **Funcionalidad**: Misma funcionalidad de predicción

## 📝 Notas Técnicas

- **Framework**: Flask 3.0.0
- **CORS**: Habilitado para compatibilidad
- **Modelo**: Carga automática al iniciar la aplicación
- **Validación**: Validación de datos en tiempo real
- **Error Handling**: Manejo robusto de errores
- **Logging**: Logs detallados para debugging

## 🤝 Contribución

Para contribuir al proyecto:

1. Fork el repositorio
2. Crea una rama para tu feature
3. Realiza los cambios
4. Envía un pull request

## 📄 Licencia

Este proyecto está bajo la misma licencia que el proyecto original.
