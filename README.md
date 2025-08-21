# 📊 Formulario de Análisis Educativo - Next.js

Una aplicación web moderna construida con Next.js para recopilar datos educativos que pueden ser procesados posteriormente con Python.

## 🚀 Características

- **Next.js 15**: Framework React moderno con App Router
- **TypeScript**: Tipado estático para mayor seguridad
- **Tailwind CSS**: Diseño responsivo y moderno
- **Validación en tiempo real**: Validación de formularios con feedback visual
- **Exportación de datos**: Copiar al portapapeles y exportar como JSON
- **Diseño responsivo**: Funciona perfectamente en móviles y escritorio
- **Animaciones suaves**: Transiciones y efectos visuales modernos

## 📋 Campos del Formulario

### Puntuaciones Académicas
- **reading_score**: Puntuación de lectura (0-100)
- **writing_score**: Puntuación de escritura (0-100)

### Información Demográfica
- **lunch**: Tipo de almuerzo (estándar/gratuito-reducido)
- **race_ethnicity_group_E**: Grupo étnico (A, B, C, D, E)
- **gender**: Género (femenino/masculino)

### Información Educativa
- **test_preparation_course**: Curso de preparación (ninguno/completado)
- **parental_level_of_education_high_school**: Nivel educativo de los padres

## 🛠️ Instalación y Uso

### Prerrequisitos
- Node.js 18+ 
- npm o yarn

### Instalación

1. **Clonar o descargar el proyecto**
2. **Instalar dependencias**:
   ```bash
   npm install
   ```

3. **Ejecutar en modo desarrollo**:
   ```bash
   npm run dev
   ```

4. **Abrir en el navegador**:
   ```
   http://localhost:3000
   ```

### Scripts disponibles

```bash
npm run dev          # Ejecutar en modo desarrollo
npm run build        # Construir para producción
npm run start        # Ejecutar en modo producción
npm run lint         # Ejecutar ESLint
```

## 📊 Procesamiento con Python

Los datos del formulario se pueden procesar fácilmente con Python. Aquí tienes un ejemplo:

```python
import json
import pandas as pd

# Cargar datos del formulario (JSON exportado)
with open('datos_educativos_2024-12-15.json', 'r', encoding='utf-8') as f:
    datos = json.load(f)

# Convertir a DataFrame de pandas
df = pd.DataFrame([datos])

# Procesar los datos
print("Datos del formulario:")
print(df)

# Análisis básico
print(f"\nPuntuación promedio de lectura: {df['reading_score'].astype(float).mean():.2f}")
print(f"Puntuación promedio de escritura: {df['writing_score'].astype(float).mean():.2f}")
```

## 🏗️ Estructura del Proyecto

```
formulario-educativo/
├── app/
│   ├── page.tsx              # Página principal
│   ├── layout.tsx            # Layout principal
│   └── globals.css           # Estilos globales
├── src/
│   ├── components/
│   │   ├── EducationalForm.tsx    # Componente del formulario
│   │   └── ResultsDisplay.tsx     # Componente de resultados
│   └── types/
│       └── index.ts              # Tipos TypeScript
├── public/                   # Archivos estáticos
├── package.json
├── tailwind.config.ts        # Configuración de Tailwind
└── tsconfig.json            # Configuración de TypeScript
```

## 🎨 Tecnologías Utilizadas

- **Next.js 15**: Framework React con App Router
- **React 18**: Biblioteca de interfaz de usuario
- **TypeScript**: Tipado estático
- **Tailwind CSS**: Framework de CSS utilitario
- **ESLint**: Linter para JavaScript/TypeScript

## 🔧 Funcionalidades Avanzadas

### Validación de Formularios
- Validación en tiempo real
- Mensajes de error específicos
- Validación de rangos numéricos
- Campos requeridos

### Exportación de Datos
- Copiar al portapapeles con un clic
- Exportar como archivo JSON
- Formato legible para análisis

### Diseño Responsivo
- Adaptable a todos los dispositivos
- Diseño móvil-first
- Navegación táctil optimizada

### Análisis de Rendimiento
- Evaluación automática de puntuaciones
- Cálculo de promedios
- Indicadores visuales de rendimiento

## 📱 Compatibilidad

- ✅ Chrome (recomendado)
- ✅ Firefox
- ✅ Safari
- ✅ Edge
- ✅ Dispositivos móviles
- ✅ Tablets

## 🚀 Despliegue

### Vercel (Recomendado)
```bash
npm run build
# Subir a Vercel
```

### Netlify
```bash
npm run build
# Configurar build command: npm run build
# Configurar publish directory: .next
```

### Docker
```dockerfile
FROM node:18-alpine
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build
EXPOSE 3000
CMD ["npm", "start"]
```

## 🤝 Contribuciones

Si quieres mejorar la aplicación, puedes:

1. Agregar nuevos campos al formulario
2. Mejorar la validación
3. Añadir más funcionalidades de exportación
4. Optimizar el rendimiento
5. Mejorar la accesibilidad

## 📄 Licencia

Este proyecto es de código abierto y está disponible bajo la licencia MIT.

## 🆘 Soporte

Si tienes problemas o preguntas:

1. Revisa la documentación de Next.js
2. Verifica que tienes Node.js 18+ instalado
3. Asegúrate de que todas las dependencias están instaladas

---

**¡Disfruta usando el formulario educativo! 🎉**
