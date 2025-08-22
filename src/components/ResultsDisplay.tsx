'use client';



interface FormData {
  reading_score: number;
  writing_score: number;
  lunch: number;
  race_ethnicity_group_E: number;
  test_preparation_course: number;
  gender: number;
  parental_level_of_education_high_school: number;
  _scaler_mean?: number[];
  _scaler_scale?: number[];
  math_score_prediction?: number;
  confidence?: number;
  model_info?: {
    type: string;
    features_used: number;
  };
}

interface ResultsDisplayProps {
  data: FormData;
  onReset: () => void;
}

export default function ResultsDisplay({ data, onReset }: ResultsDisplayProps) {

  return (
    <div className="p-8">
      <div className="text-center mb-8">
        <h2 className="text-3xl font-bold text-slate-800 mb-4">
          📋 Datos Enviados Exitosamente
        </h2>
        <p className="text-slate-600">
          Los datos han sido procesados y la predicción está lista
        </p>
      </div>

      {/* Predicción del Math Score */}    
        <div className="bg-gradient-to-br from-purple-50 to-purple-100 p-8 rounded-xl border border-purple-200 text-center mb-8">
          <h3 className="text-2xl font-bold text-purple-800 mb-4">
            🧮 Predicción de Matemáticas
          </h3>
          <p className="text-5xl font-bold text-purple-600 mb-4">
            {data.math_score_prediction}
          </p>
          <span className="inline-block px-4 py-2 rounded-full text-lg font-medium bg-purple-100 text-purple-600">
            {data.confidence ? `Confianza: ${(data.confidence * 100).toFixed(1)}%` : 'Predicción con Machine Learning'}
          </span>
        </div>
  

      {/* Botón para nuevo formulario */}
      <div className="flex justify-center">
        <button
          onClick={onReset}
          className="px-8 py-4 bg-indigo-500 hover:bg-indigo-600 text-white font-semibold rounded-lg transform hover:scale-105 transition-all duration-200 shadow-lg"
        >
          🔄 Nuevo Formulario
        </button>
      </div>
    </div>
  );
}
