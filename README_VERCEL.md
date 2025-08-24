# 🚀 Deployment de Flask en Vercel

Este proyecto está configurado para ser desplegado en Vercel con archivos estáticos.

## 📂 Estructura del Proyecto

```
formulario-educativo/
├── app/
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css
│   │   └── js/
│   │       └── app.js
│   ├── templates/
│   │   └── index.html
│   ├── models/
│   │   └── lin_reg_model_opt.pkl
│   └── app.py
├── .gitignore
├── requirements.txt
├── vercel.json
└── README_VERCEL.md
```

## ⚙️ Configuración de Vercel

### vercel.json
```json
{
  "version": 2,
  "builds": [
    {
      "src": "app/app.py",
      "use": "@vercel/python"
    },
    {
      "src": "app/static/**/*",
      "use": "@vercel/static"
    }
  ],
  "routes": [
    {
      "src": "/app/static/(.*)",
      "dest": "/app/static/$1"
    },
    {
      "src": "/(.*)",
      "dest": "app/app.py"
    }
  ]
}
```

## 📋 Pasos para el Deployment

### 1. Preparar el Proyecto
- Asegúrate de que todos los archivos estén en su lugar correcto
- Verifica que `requirements.txt` contenga todas las dependencias necesarias
- Confirma que el modelo `lin_reg_model_opt.pkl` esté en `app/models/`

### 2. Conectar con Vercel
```bash
# Instalar Vercel CLI (si no lo tienes)
npm i -g vercel

# Iniciar sesión en Vercel
vercel login

# Desplegar el proyecto
vercel
```

### 3. Configuración en Vercel Dashboard
1. Ve a tu dashboard de Vercel
2. Selecciona tu proyecto
3. Ve a Settings > General
4. Configura las variables de entorno si es necesario

## 🔧 Archivos Estáticos

### CSS (`app/static/css/style.css`)
- Estilos básicos para la aplicación
- Diseño responsive
- Colores y tipografía consistentes

### JavaScript (`app/static/js/app.js`)
- Validación de formularios
- Manejo de errores
- Funciones de utilidad

### HTML (`app/templates/index.html`)
- Template principal de la aplicación
- Referencias a archivos estáticos usando rutas relativas
- Formulario de predicción

## 🌐 Rutas de Archivos Estáticos

En el HTML, los archivos estáticos se referencian así:
```html
<link rel="stylesheet" href="/app/static/css/style.css">
<script src="/app/static/js/app.js"></script>
```

## ✅ Verificación del Deployment

1. **Página principal**: `https://tu-proyecto.vercel.app/`
2. **Archivos estáticos**: 
   - CSS: `https://tu-proyecto.vercel.app/app/static/css/style.css`
   - JS: `https://tu-proyecto.vercel.app/app/static/js/app.js`
3. **API de predicción**: `https://tu-proyecto.vercel.app/predict`

## 🐛 Solución de Problemas

### Error: "Module not found"
- Verifica que `requirements.txt` contenga todas las dependencias
- Asegúrate de que las versiones sean compatibles

### Error: "Static files not found"
- Confirma que la estructura de carpetas sea correcta
- Verifica que `vercel.json` tenga la configuración de archivos estáticos

### Error: "Model not found"
- Asegúrate de que `lin_reg_model_opt.pkl` esté en `app/models/`
- Verifica que el archivo no esté corrupto

## 📝 Notas Importantes

1. **Rutas de archivos estáticos**: Deben usar `/app/static/` como prefijo
2. **Templates**: Deben estar en `app/templates/`
3. **Modelo**: Debe estar en `app/models/`
4. **Archivo principal**: Debe ser `app/app.py`

## 🔄 Actualizaciones

Para actualizar el deployment:
```bash
vercel --prod
```

## 📞 Soporte

Si encuentras problemas:
1. Revisa los logs en Vercel Dashboard
2. Verifica la configuración de `vercel.json`
3. Confirma que la estructura de archivos sea correcta
