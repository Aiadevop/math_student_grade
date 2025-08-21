'use client';

import { useState } from 'react';

interface FormData {
  reading_score: string;
  writing_score: string;
  lunch: string;
  race_ethnicity_group_E: string;
  test_preparation_course: string;
  gender: string;
  parental_level_of_education_high_school: string;
}

interface ResultsDisplayProps {
  data: FormData;
  onReset: () => void;
}

export default function ResultsDisplay({ data, onReset }: ResultsDisplayProps) {
  const [copied, setCopied] = useState(false);

  const fieldNames = {
    reading_score: '📖 Puntuación de Lectura',
    writing_score: '✍️ Puntuación de Escritura',
    lunch: '🍽️ Tipo de Almuerzo',
    race_ethnicity_group_E: '👥 Grupo Étnico',
    test_preparation_course: '📚 Curso de Preparación',
    gender: '👤 Género',
    parental_level_of_education_high_school: '🎓 Nivel Educativo de los Padres'
  };

  const formatDataForDisplay = () => {
    const transformedData = transformDataForAnalysis();
    
    let content = '📊 DATOS DEL FORMULARIO\n';
    content += '='.repeat(30) + '\n\n';
    
    // Datos originales
    content += '📝 DATOS ORIGINALES:\n';
    content += '-'.repeat(20) + '\n';
    Object.entries(data).forEach(([key, value]) => {
      const displayName = fieldNames[key as keyof typeof fieldNames] || key;
      content += `${displayName}: ${value}\n`;
    });
    
    content += '\n🔢 DATOS TRANSFORMADOS PARA ANÁLISIS:\n';
    content += '-'.repeat(30) + '\n';
    Object.entries(transformedData).forEach(([key, value]) => {
      const displayName = fieldNames[key as keyof typeof fieldNames] || key;
      content += `${displayName}: ${value}\n`;
    });
    
    content += `\n📅 Fecha: ${new Date().toLocaleString('es-ES')}`;
    
    return content;
  };

  const copyToClipboard = async () => {
    try {
      const text = formatDataForDisplay();
      await navigator.clipboard.writeText(text);
      setCopied(true);
      setTimeout(() => setCopied(false), 2000);
    } catch (err) {
      console.error('Error al copiar:', err);
      // Fallback para navegadores más antiguos
      const textArea = document.createElement('textarea');
      textArea.value = formatDataForDisplay();
      document.body.appendChild(textArea);
      textArea.select();
      document.execCommand('copy');
      document.body.removeChild(textArea);
      setCopied(true);
      setTimeout(() => setCopied(false), 2000);
    }
  };

  const transformDataForAnalysis = () => {
    // Transformar datos según las especificaciones
    const transformedData = {
      reading_score: parseFloat(data.reading_score),
      writing_score: parseFloat(data.writing_score),
      lunch: data.lunch === 'standard' ? 1 : 0,
      test_preparation_course: data.test_preparation_course === 'completed' ? 1 : 0,
      gender: data.gender === 'male' ? 1 : 0,
      race_ethnicity_group_E: data.race_ethnicity_group_E === 'group E' ? 1 : 0,
      parental_level_of_education_high_school: data.parental_level_of_education_high_school === 'high school' ? 1 : 0
    };
    return transformedData;
  };

  const exportAsJSON = () => {
    const transformedData = transformDataForAnalysis();
    const jsonString = JSON.stringify(transformedData, null, 2);
    const blob = new Blob([jsonString], { type: 'application/json' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `datos_educativos_${new Date().toISOString().split('T')[0]}.json`;
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
  };

  const calculateAverage = () => {
    const reading = parseFloat(data.reading_score);
    const writing = parseFloat(data.writing_score);
    return ((reading + writing) / 2).toFixed(1);
  };

  const getPerformanceLevel = (score: number) => {
    if (score >= 90) return { level: 'Excelente', color: 'text-blue-600', bg: 'bg-blue-100' };
    if (score >= 80) return { level: 'Bueno', color: 'text-teal-600', bg: 'bg-teal-100' };
    if (score >= 70) return { level: 'Promedio', color: 'text-indigo-600', bg: 'bg-indigo-100' };
    return { level: 'Necesita mejorar', color: 'text-slate-600', bg: 'bg-slate-100' };
  };

  const readingPerformance = getPerformanceLevel(parseFloat(data.reading_score));
  const writingPerformance = getPerformanceLevel(parseFloat(data.writing_score));

  return (
    <div className="p-8">
      <div className="text-center mb-8">
        <h2 className="text-3xl font-bold text-slate-800 mb-4">
          📋 Datos Enviados Exitosamente
        </h2>
        <p className="text-slate-600">
          Los datos han sido procesados y están listos para análisis
        </p>
      </div>

      {/* Resumen de puntuaciones */}
      <div className="grid md:grid-cols-3 gap-6 mb-8">
        <div className="bg-gradient-to-br from-blue-50 to-blue-100 p-6 rounded-xl border border-blue-200">
          <h3 className="text-lg font-semibold text-blue-800 mb-2">📖 Lectura</h3>
          <p className="text-3xl font-bold text-blue-600">{data.reading_score}</p>
          <span className={`inline-block px-3 py-1 rounded-full text-sm font-medium ${readingPerformance.bg} ${readingPerformance.color}`}>
            {readingPerformance.level}
          </span>
        </div>

        <div className="bg-gradient-to-br from-teal-50 to-teal-100 p-6 rounded-xl border border-teal-200">
          <h3 className="text-lg font-semibold text-teal-800 mb-2">✍️ Escritura</h3>
          <p className="text-3xl font-bold text-teal-600">{data.writing_score}</p>
          <span className={`inline-block px-3 py-1 rounded-full text-sm font-medium ${writingPerformance.bg} ${writingPerformance.color}`}>
            {writingPerformance.level}
          </span>
        </div>

        <div className="bg-gradient-to-br from-indigo-50 to-indigo-100 p-6 rounded-xl border border-indigo-200">
          <h3 className="text-lg font-semibold text-indigo-800 mb-2">📊 Promedio</h3>
          <p className="text-3xl font-bold text-indigo-600">{calculateAverage()}</p>
          <span className="inline-block px-3 py-1 rounded-full text-sm font-medium bg-indigo-100 text-indigo-600">
            General
          </span>
        </div>
      </div>

      {/* Datos completos */}
      <div className="bg-slate-50 rounded-xl p-6 mb-8">
        <h3 className="text-xl font-bold text-slate-800 mb-4 flex items-center gap-2">
          📊 Datos Completos del Formulario
        </h3>
        
        <div className="grid md:grid-cols-2 gap-6">
          {Object.entries(data).map(([key, value]) => (
            <div key={key} className="bg-white p-4 rounded-lg border border-slate-200">
              <dt className="text-sm font-medium text-slate-500 mb-1">
                {fieldNames[key as keyof typeof fieldNames] || key}
              </dt>
              <dd className="text-lg font-semibold text-slate-900">{value}</dd>
            </div>
          ))}
        </div>
      </div>

             {/* Datos transformados para análisis */}
       <div className="bg-blue-50 rounded-xl p-6 mb-8 border border-blue-200">
         <h3 className="text-xl font-bold text-blue-800 mb-4 flex items-center gap-2">
           🔢 Datos Transformados para Análisis
         </h3>
         <div className="grid md:grid-cols-2 gap-6">
           {Object.entries(transformDataForAnalysis()).map(([key, value]) => (
             <div key={key} className="bg-white p-4 rounded-lg border border-blue-200">
               <dt className="text-sm font-medium text-blue-600 mb-1">
                 {fieldNames[key as keyof typeof fieldNames] || key}
               </dt>
               <dd className="text-lg font-bold text-blue-800">{value}</dd>
             </div>
           ))}
         </div>
       </div>

       {/* Datos en formato texto */}
       <div className="bg-teal-50 rounded-xl p-6 mb-8 border border-teal-200">
         <h3 className="text-xl font-bold text-teal-800 mb-4 flex items-center gap-2">
           📝 Datos Formateados
         </h3>
         <pre className="bg-white p-4 rounded-lg border border-teal-200 text-sm font-mono text-slate-800 whitespace-pre-wrap overflow-x-auto">
           {formatDataForDisplay()}
         </pre>
       </div>

      {/* Botones de acción */}
      <div className="flex flex-col sm:flex-row gap-4 justify-center">
        <button
          onClick={copyToClipboard}
          className={`px-6 py-3 rounded-lg font-semibold transition-all duration-200 shadow-lg ${
            copied 
              ? 'bg-blue-500 text-white' 
              : 'bg-blue-500 hover:bg-blue-600 text-white transform hover:scale-105'
          }`}
        >
          {copied ? '✅ Copiado!' : '📋 Copiar Datos'}
        </button>
        
        <button
          onClick={exportAsJSON}
          className="px-6 py-3 bg-teal-500 hover:bg-teal-600 text-white font-semibold rounded-lg transform hover:scale-105 transition-all duration-200 shadow-lg"
        >
          💾 Exportar JSON
        </button>
        
        <button
          onClick={onReset}
          className="px-6 py-3 bg-indigo-500 hover:bg-indigo-600 text-white font-semibold rounded-lg transform hover:scale-105 transition-all duration-200 shadow-lg"
        >
          🔄 Nuevo Formulario
        </button>
      </div>

      {/* Información adicional */}
      <div className="mt-8 p-4 bg-blue-50 rounded-lg border border-blue-200">
        <h4 className="font-semibold text-blue-800 mb-2">💡 Información</h4>
        <p className="text-blue-700 text-sm">
          Los datos están listos para ser procesados con Python. Puedes copiarlos al portapapeles 
          o exportarlos como JSON para su análisis posterior.
        </p>
      </div>
    </div>
  );
}
