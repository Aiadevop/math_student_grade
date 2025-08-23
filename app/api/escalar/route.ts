import { NextRequest, NextResponse } from 'next/server';
import { spawn } from 'child_process';
import path from 'path';

export async function POST(request: NextRequest) {
  try {
    console.log('🌐 API de validación recibida');
    
    // Obtener datos del formulario
    const datos = await request.json();
    console.log('📥 Datos recibidos:', datos);
    
    // Validar que estén las variables necesarias
    const variables_requeridas = ['reading_score', 'writing_score', 'lunch', 
                                'race_ethnicity_group_E', 'test_preparation_course', 
                                'gender', 'parental_level_of_education_high_school'];
    
    for (const var_name of variables_requeridas) {
      if (!(var_name in datos)) {
        console.error(`❌ Variable faltante: ${var_name}`);
        return NextResponse.json(
          { error: `Variable faltante: ${var_name}` },
          { status: 400 }
        );
      }
    }
    
    console.log('✅ Todas las variables están presentes');
    
    // Convertir datos a JSON string
    const datosJson = JSON.stringify(datos);
    console.log('📤 Enviando datos para validación:', datosJson);
    
    // Ruta al script de Python
    const scriptPath = path.join(process.cwd(), 'validar_datos.py');
    console.log('🐍 Ruta del script Python:', scriptPath);
    
    // Ejecutar script de Python
    const resultado = await ejecutarScriptPython(scriptPath, datosJson);
    console.log('✅ Datos validados:', resultado);
    
    return NextResponse.json(resultado);
    
  } catch (error) {
    console.error('❌ Error en API de validación:', error);
    return NextResponse.json(
      { error: 'Error interno del servidor' },
      { status: 500 }
    );
  }
}

function ejecutarScriptPython(scriptPath: string, datosJson: string): Promise<Record<string, unknown>> {
  return new Promise((resolve, reject) => {
    // Ejecutar script de Python
    const pythonProcess = spawn('python', [scriptPath], {
      stdio: ['pipe', 'pipe', 'pipe']
    });
    
    let resultado = '';
    let error = '';
    
    // Enviar datos al script
    pythonProcess.stdin.write(datosJson);
    pythonProcess.stdin.end();
    
    // Capturar salida
    pythonProcess.stdout.on('data', (data) => {
      resultado += data.toString();
    });
    
    // Capturar errores
    pythonProcess.stderr.on('data', (data) => {
      error += data.toString();
    });
    
    // Manejar finalización
    pythonProcess.on('close', (code) => {
      if (code === 0) {
        try {
          const datosEscalados = JSON.parse(resultado.trim());
          resolve(datosEscalados);
        } catch (parseError) {
          reject(new Error(`Error al parsear resultado: ${parseError}`));
        }
      } else {
        reject(new Error(`Script de Python falló con código ${code}: ${error}`));
      }
    });
    
    // Manejar errores del proceso
    pythonProcess.on('error', (err) => {
      reject(new Error(`Error al ejecutar script de Python: ${err.message}`));
    });
  });
}
