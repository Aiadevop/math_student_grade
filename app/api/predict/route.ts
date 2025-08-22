import { NextRequest, NextResponse } from 'next/server';
import { spawn } from 'child_process';
import path from 'path';

export async function POST(request: NextRequest) {
  try {
    console.log('🎯 API de predicción recibida');
    
    const datosEscalados = await request.json();
    console.log('📥 Datos escalados recibidos:', datosEscalados);
    
    // Verificar que tenemos los datos escalados necesarios
    const variablesRequeridas = [
      'gender', 'lunch', 'test_preparation_course', 'reading_score', 
      'writing_score', 'race_ethnicity_group_E', 'parental_level_of_education_high_school'
    ];
    
    const faltantes = variablesRequeridas.filter(varName => 
      datosEscalados[varName] === undefined || datosEscalados[varName] === null
    );
    
    if (faltantes.length > 0) {
      console.error('❌ Variables faltantes:', faltantes);
      return NextResponse.json(
        { error: `Variables faltantes: ${faltantes.join(', ')}` },
        { status: 400 }
      );
    }
    
    console.log('✅ Todas las variables están presentes');
    
    // Preparar datos para el modelo (en el orden correcto)
    const datosParaModelo = [
      datosEscalados.gender,
      datosEscalados.lunch,
      datosEscalados.test_preparation_course,
      datosEscalados.reading_score,
      datosEscalados.writing_score,
      datosEscalados.race_ethnicity_group_E,
      datosEscalados.parental_level_of_education_high_school
    ];
    
    console.log('📤 Enviando datos al modelo:', datosParaModelo);
    
    // Ejecutar script de Python para predicción
    const scriptPath = path.join(process.cwd(), 'predict_math_score.py');
    console.log('🐍 Ruta del script Python:', scriptPath);
    
    const pythonProcess = spawn('python', [scriptPath, JSON.stringify(datosParaModelo)]);
    
    let resultado = '';
    let errorOutput = '';
    
    pythonProcess.stdout.on('data', (data) => {
      resultado += data.toString();
    });
    
    pythonProcess.stderr.on('data', (data) => {
      errorOutput += data.toString();
    });
    
    return new Promise<NextResponse>((resolve) => {
      pythonProcess.on('close', (code) => {
        console.log('🐍 Proceso Python terminado con código:', code);
        
        if (code !== 0) {
          console.error('❌ Error en Python:', errorOutput);
          resolve(NextResponse.json(
            { error: `Error en predicción: ${errorOutput}` },
            { status: 500 }
          ));
          return;
        }
        
        try {
          const prediccion = JSON.parse(resultado.trim());
          console.log('✅ Predicción recibida:', prediccion);
          
          // Agregar los datos escalados originales al resultado
          const resultadoCompleto = {
            ...datosEscalados,
            math_score_prediction: prediccion.math_score,
            confidence: prediccion.confidence || null
          };
          
          resolve(NextResponse.json(resultadoCompleto));
        } catch (parseError) {
          console.error('❌ Error al parsear resultado:', parseError);
          resolve(NextResponse.json(
            { error: 'Error al procesar la predicción' },
            { status: 500 }
          ));
        }
      });
    });
    
  } catch (error) {
    console.error('❌ Error en API de predicción:', error);
    return NextResponse.json(
      { error: 'Error interno del servidor' },
      { status: 500 }
    );
  }
}

