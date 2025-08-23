#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Aplicación Flask para predicción de calificaciones matemáticas
Punto de entrada principal para Vercel
"""

import sys
import os

# Agregar el directorio actual al path para que Python pueda encontrar el módulo app
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app.app import app

if __name__ == '__main__':
    app.run(debug=False)
