'use client';

import { useState } from 'react';
import EducationalForm from '../src/components/EducationalForm';
import ResultsDisplay from '../src/components/ResultsDisplay';

export default function Home() {
  const [formData, setFormData] = useState<any>(null);
  const [showResults, setShowResults] = useState(false);

  const handleFormSubmit = (data: any) => {
    setFormData(data);
    setShowResults(true);
  };

  const handleReset = () => {
    setFormData(null);
    setShowResults(false);
  };

  return (
    <main className="min-h-screen bg-gradient-to-br from-slate-400 via-blue-300 to-indigo-300 p-4">
      <div className="max-w-4xl mx-auto">
        <header className="text-center text-slate-800 mb-8">
          <h1 className="text-4xl md:text-5xl font-bold mb-4">
            Formulario de Análisis Educativo
          </h1>
          <p className="text-xl text-slate-600">
            Introduce los datos para predecir tu nota de matemáticas
          </p>
        </header>

        <div className="bg-white rounded-2xl shadow-2xl overflow-hidden">
          {!showResults ? (
            <EducationalForm onSubmit={handleFormSubmit} />
          ) : (
            <ResultsDisplay 
              data={formData} 
              onReset={handleReset}
            />
          )}
        </div>
      </div>
    </main>
  );
}
