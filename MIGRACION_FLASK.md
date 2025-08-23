# 🔄 Migración de Next.js a Flask - Guía Completa

Esta guía te ayudará a migrar tu aplicación de predicción de calificaciones matemáticas de Next.js a Flask para que funcione correctamente en Vercel.

## 📋 Resumen de la Migración

### ✅ Lo que se ha migrado:
- **API Routes** → **Endpoints Flask**
- **Validación de datos** → **Funciones Python**
- **Modelo ML** → **Mismo modelo (lin_reg_model_opt.pkl)**
- **Interfaz web** → **HTML integrado con Tailwind CSS**
- **Funcionalidad completa** → **100% preservada**

### 🆕 Nuevos archivos creados:
- `app.py` - Aplicación Flask principal
- `wsgi.py` - Archivo WSGI para servidores
- `requirements_flask.txt` - Dependencias de Python
- `vercel.json` - Configuración de Vercel
- `test_flask_app.py` - Script de pruebas
- `setup_flask.py` - Script de configuración
- `README_FLASK.md` - Documentación específica

## 🚀 Pasos para la Migración

### 1. Preparación del Entorno

```bash
# Verificar que tienes Python 3.8+
python --version

# Ejecutar el script de configuración
python setup_flask.py
```

### 2. Instalación de Dependencias

```bash
# Instalar dependencias de Flask
pip install -r requirements_flask.txt
```

### 3. Verificación del Modelo

Asegúrate de que el archivo `lin_reg_model_opt.pkl` esté en la carpeta `models/`:

```bash
# Verificar que el modelo existe
ls -la models/lin_reg_model_opt.pkl
```

### 4. Pruebas Locales

```bash
# Ejecutar la aplicación Flask
python app.py

# En otra terminal, ejecutar las pruebas
python test_flask_app.py
```

### 5. Despliegue en Vercel

1. **Subir a GitHub**:
   ```bash
   git add .
   git commit -m "Migración a Flask completada"
   git push origin main
   ```

2. **Conectar con Vercel**:
   - Ve a [vercel.com](https://vercel.com)
   - Importa tu repositorio de GitHub
   - Vercel detectará automáticamente la configuración de Python

## 🔄 Mapeo de Endpoints

| Next.js | Flask | Descripción |
|---------|-------|-------------|
| `/api/escalar` | `/api/escalar` | Validación de datos |
| `/api/predict` | `/api/predict` | Predicción (API) |
| - | `/predict` | Predicción (directa) |
| - | `/health` | Verificación de salud |
| `/` | `/` | Página principal |

## 📊 Comparación de Funcionalidades

### ✅ Funcionalidades Preservadas:
- ✅ Validación de 7 variables requeridas
- ✅ Carga del modelo `lin_reg_model_opt.pkl`
- ✅ Predicción de calificaciones matemáticas
- ✅ Manejo de errores robusto
- ✅ Interfaz web moderna
- ✅ API REST completa

### 🆕 Mejoras en Flask:
- 🚀 **Mejor rendimiento** en Vercel
- 🔧 **Configuración más simple**
- 📦 **Menos dependencias**
- 🐍 **Nativo en Python**
- 🔍 **Logs más detallados**

## 🛠️ Solución de Problemas

### Error: "Modelo no disponible"
```bash
# Verificar que el modelo existe
ls -la models/lin_reg_model_opt.pkl

# Verificar permisos
chmod 644 models/lin_reg_model_opt.pkl
```

### Error: "Variable faltante"
- Verifica que todas las variables estén presentes en la petición
- Asegúrate de que los valores sean numéricos

### Error de despliegue en Vercel
```bash
# Verificar configuración
cat vercel.json

# Verificar dependencias
cat requirements_flask.txt
```

## 📝 Ejemplo de Uso

### Usando la API:
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

### Respuesta esperada:
```json
{
  "gender": 1.0,
  "lunch": 1.0,
  "test_preparation_course": 1.0,
  "reading_score": 85.5,
  "writing_score": 82.3,
  "race_ethnicity_group_E": 0.0,
  "parental_level_of_education_high_school": 1.0,
  "math_score_prediction": 87.23,
  "confidence": 0.872,
  "model_info": {
    "type": "LinearRegression",
    "features_used": 7
  }
}
```

## 🔧 Configuración Avanzada

### Variables de Entorno (Opcional):
```bash
# Para desarrollo local
export FLASK_ENV=development
export FLASK_DEBUG=1

# Para producción
export FLASK_ENV=production
export FLASK_DEBUG=0
```

### Personalización del Modelo:
El modelo se carga automáticamente desde estas ubicaciones (en orden):
1. `models/lin_reg_model_opt.pkl` (recomendado)
2. `model/lin_reg_model_opt.pkl`
3. `lin_reg_model_opt.pkl` (fallback)

## 📈 Monitoreo y Logs

### Logs de la Aplicación:
```bash
# Ver logs en tiempo real
tail -f logs/app.log

# Ver logs de Vercel
vercel logs
```

### Endpoint de Salud:
```bash
curl http://localhost:5000/health
```

Respuesta:
```json
{
  "status": "healthy",
  "model_loaded": true,
  "model_path": "lin_reg_model_opt.pkl"
}
```

## 🎯 Ventajas de la Migración

1. **Mejor Compatibilidad con Vercel**: Flask es nativo de Python
2. **Menor Overhead**: Sin necesidad de Node.js
3. **Configuración Más Simple**: Menos archivos de configuración
4. **Mejor Rendimiento**: Carga más rápida del modelo
5. **Logs Más Claros**: Mejor debugging

## 🔄 Rollback (Si es necesario)

Si necesitas volver a Next.js:

```bash
# Restaurar archivos originales
git checkout HEAD~1 -- app/
git checkout HEAD~1 -- package.json
git checkout HEAD~1 -- next.config.ts

# Eliminar archivos de Flask
rm app.py wsgi.py requirements_flask.txt vercel.json
```

## 📞 Soporte

Si encuentras problemas durante la migración:

1. Revisa los logs de la aplicación
2. Ejecuta `python test_flask_app.py`
3. Verifica la configuración de Vercel
4. Consulta la documentación en `README_FLASK.md`

## ✅ Checklist de Migración

- [ ] Ejecutar `python setup_flask.py`
- [ ] Verificar que `models/lin_reg_model_opt.pkl` existe
- [ ] Probar localmente con `python app.py`
- [ ] Ejecutar pruebas con `python test_flask_app.py`
- [ ] Subir código a GitHub
- [ ] Conectar repositorio en Vercel
- [ ] Verificar despliegue exitoso
- [ ] Probar funcionalidad en producción

¡La migración está completa! 🎉
