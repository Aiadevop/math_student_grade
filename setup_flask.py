#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de configuración para la aplicación Flask
"""

import os
import sys
import subprocess
import shutil
from pathlib import Path

def check_python_version():
    """
    Verificar la versión de Python
    """
    print("🐍 Verificando versión de Python...")
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print("❌ Se requiere Python 3.8 o superior")
        print(f"   Versión actual: {version.major}.{version.minor}.{version.micro}")
        return False
    print(f"✅ Python {version.major}.{version.minor}.{version.micro} - Compatible")
    return True

def check_model_file():
    """
    Verificar que el archivo del modelo existe
    """
    print("\n📊 Verificando archivo del modelo...")
    model_paths = [
        'models/lin_reg_model_opt.pkl',  # Primera opción: carpeta models
        'model/lin_reg_model_opt.pkl',
        'lin_reg_model_opt.pkl'          # Fallback: raíz del proyecto
    ]
    
    for path in model_paths:
        if Path(path).exists():
            print(f"✅ Modelo encontrado en: {path}")
            return True
    
    print("❌ No se encontró el archivo lin_reg_model_opt.pkl")
    print("   Asegúrate de que el archivo esté en la raíz del proyecto")
    return False

def install_dependencies():
    """
    Instalar dependencias de Python
    """
    print("\n📦 Instalando dependencias...")
    try:
        subprocess.check_call([
            sys.executable, "-m", "pip", "install", "-r", "requirements_flask.txt"
        ])
        print("✅ Dependencias instaladas correctamente")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error al instalar dependencias: {e}")
        return False

def test_model_loading():
    """
    Probar la carga del modelo
    """
    print("\n🧪 Probando carga del modelo...")
    try:
        # Importar las funciones necesarias
        sys.path.append('.')
        from app import cargar_modelo
        
        modelo, ruta = cargar_modelo()
        print(f"✅ Modelo cargado exitosamente desde: {ruta}")
        print(f"   Tipo de modelo: {type(modelo).__name__}")
        return True
    except Exception as e:
        print(f"❌ Error al cargar el modelo: {e}")
        return False

def create_directories():
    """
    Crear directorios necesarios
    """
    print("\n📁 Creando directorios necesarios...")
    directories = ['logs', 'temp']
    
    for directory in directories:
        Path(directory).mkdir(exist_ok=True)
        print(f"✅ Directorio creado: {directory}")

def check_files():
    """
    Verificar que todos los archivos necesarios existen
    """
    print("\n📋 Verificando archivos necesarios...")
    required_files = [
        'app.py',
        'wsgi.py',
        'requirements_flask.txt',
        'vercel.json'
    ]
    
    missing_files = []
    for file in required_files:
        if Path(file).exists():
            print(f"✅ {file}")
        else:
            print(f"❌ {file} - Faltante")
            missing_files.append(file)
    
    if missing_files:
        print(f"\n⚠️ Archivos faltantes: {', '.join(missing_files)}")
        return False
    
    return True

def main():
    """
    Función principal de configuración
    """
    print("🚀 Configuración de la aplicación Flask")
    print("=" * 50)
    
    # Verificar versión de Python
    if not check_python_version():
        return False
    
    # Verificar archivo del modelo
    if not check_model_file():
        return False
    
    # Verificar archivos necesarios
    if not check_files():
        return False
    
    # Crear directorios
    create_directories()
    
    # Instalar dependencias
    if not install_dependencies():
        return False
    
    # Probar carga del modelo
    if not test_model_loading():
        return False
    
    print("\n" + "=" * 50)
    print("🎉 Configuración completada exitosamente!")
    print("\n📝 Próximos pasos:")
    print("1. Ejecutar la aplicación: python app.py")
    print("2. Abrir en el navegador: http://localhost:5000")
    print("3. Para pruebas: python test_flask_app.py")
    print("\n🚀 Para desplegar en Vercel:")
    print("1. Subir el código a GitHub")
    print("2. Conectar el repositorio en Vercel")
    print("3. ¡Listo!")
    
    return True

if __name__ == "__main__":
    success = main()
    if not success:
        print("\n❌ La configuración falló. Revisa los errores anteriores.")
        sys.exit(1)
