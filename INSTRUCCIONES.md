# 🚀 Instrucciones Rápidas - Formulario Educativo Next.js

## ⚡ Inicio Rápido

### 1. Ejecutar la aplicación
```bash
cd formulario-educativo
npm run dev
```

### 2. Abrir en el navegador
```
http://localhost:3000
```

## 📝 Cómo usar el formulario

### Paso 1: Llenar el formulario
1. **Puntuaciones Académicas**: Introduce las puntuaciones de lectura y escritura (0-100)
2. **Información Demográfica**: Selecciona tipo de almuerzo, grupo étnico y género
3. **Información Educativa**: Indica el curso de preparación y nivel educativo de los padres

### Paso 2: Enviar datos
- Haz clic en "📤 Enviar Datos"
- Los datos se validarán automáticamente
- Si hay errores, se mostrarán en rojo

### Paso 3: Ver resultados
- Se mostrará un resumen de las puntuaciones
- Evaluación automática del rendimiento
- Datos formateados para copiar

### Paso 4: Exportar datos
- **📋 Copiar Datos**: Copia al portapapeles
- **💾 Exportar JSON**: Descarga archivo JSON
- **🔄 Nuevo Formulario**: Limpia y empieza de nuevo

## 🐍 Procesar con Python

### Opción 1: Usar el script incluido
```bash
python procesar_datos_nextjs.py
```

### Opción 2: Procesar manualmente
```python
import json
import pandas as pd

# Cargar datos del JSON exportado
with open('datos_educativos_2024-12-15.json', 'r') as f:
    datos = json.load(f)

# Convertir a DataFrame
df = pd.DataFrame([datos])
print(df)
```

## 🔧 Solución de problemas

### Error: "npm run dev no funciona"
```bash
# Verificar Node.js
node --version  # Debe ser 18+

# Reinstalar dependencias
rm -rf node_modules package-lock.json
npm install
```

### Error: "Puerto 3000 ocupado"
```bash
# Usar otro puerto
npm run dev -- -p 3001
```

### Error: "No se pueden copiar datos"
- Asegúrate de usar HTTPS o localhost
- Algunos navegadores requieren permisos de portapapeles

## 📱 Características móviles

- ✅ Diseño responsivo automático
- ✅ Navegación táctil optimizada
- ✅ Campos adaptados para móviles
- ✅ Botones de tamaño adecuado

## 🎯 Campos del formulario

| Campo | Tipo | Rango/Opciones |
|-------|------|----------------|
| reading_score | Número | 0-100 |
| writing_score | Número | 0-100 |
| lunch | Select | Estándar / Gratuito-Reducido |
| race_ethnicity_group_E | Select | Grupo A, B, C, D, E |
| gender | Select | Femenino / Masculino |
| test_preparation_course | Select | Ninguno / Completado |
| parental_level_of_education_high_school | Select | 6 opciones educativas |

## 🚀 Despliegue

### Vercel (Recomendado)
```bash
npm run build
# Subir a Vercel
```

### Netlify
```bash
npm run build
# Configurar build: npm run build
# Configurar publish: .next
```

---

**¡Listo para usar! 🎉**

