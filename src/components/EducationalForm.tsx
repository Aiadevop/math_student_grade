'use client';

import { useState } from 'react';
import { FormData, FormErrors } from '../types';

interface EducationalFormProps {
  onSubmit: (data: FormData) => void;
}

export default function EducationalForm({ onSubmit }: EducationalFormProps) {
  const [formData, setFormData] = useState<Partial<FormData>>({
    reading_score: undefined,
    writing_score: undefined,
    lunch: 1,
    race_ethnicity_group_E: 0,
    test_preparation_course: 0,
    gender: 0,
    parental_level_of_education_high_school: 0
  });

  const [errors, setErrors] = useState<FormErrors>({});

  const handleInputChange = (field: keyof FormData, value: number | undefined) => {
    setFormData(prev => ({ ...prev, [field]: value }));
    // Clear error when user starts typing
    if (errors[field]) {
      setErrors(prev => ({ ...prev, [field]: undefined }));
    }
  };

  const validateForm = (): boolean => {
    const newErrors: FormErrors = {};

    // Solo validar las puntuaciones académicas como campos obligatorios
    if (formData.reading_score === undefined || formData.reading_score === null) {
      newErrors.reading_score = 0; // Usar 0 como valor de error para indicar campo requerido
    }

    if (formData.writing_score === undefined || formData.writing_score === null) {
      newErrors.writing_score = 0; // Usar 0 como valor de error para indicar campo requerido
    }

    // Validar que las puntuaciones estén en el rango correcto (incluyendo 0)
    if (formData.reading_score !== undefined && formData.reading_score !== null && (formData.reading_score < 0 || formData.reading_score > 100)) {
      newErrors.reading_score = formData.reading_score;
    }

    if (formData.writing_score !== undefined && formData.writing_score !== null && (formData.writing_score < 0 || formData.writing_score > 100)) {
      newErrors.writing_score = formData.writing_score;
    }

    setErrors(newErrors);
    return Object.keys(newErrors).length === 0;
  };

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    
    if (validateForm()) {
      // Asegurar que todos los campos tengan valores numéricos válidos
      const completeData: FormData = {
        reading_score: formData.reading_score !== undefined && formData.reading_score !== null ? formData.reading_score : 0,
        writing_score: formData.writing_score !== undefined && formData.writing_score !== null ? formData.writing_score : 0,
        lunch: formData.lunch || 0,
        race_ethnicity_group_E: formData.race_ethnicity_group_E || 0,
        test_preparation_course: formData.test_preparation_course || 0,
        gender: formData.gender || 0,
        parental_level_of_education_high_school: formData.parental_level_of_education_high_school || 0
      };
      onSubmit(completeData);
    }
  };

  const handleReset = () => {
    setFormData({
      reading_score: undefined,
      writing_score: undefined,
      lunch: 1,
      race_ethnicity_group_E: 0,
      test_preparation_course: 0,
      gender: 0,
      parental_level_of_education_high_school: 0
    });
    setErrors({});
  };

  return (
    <form onSubmit={handleSubmit} className="p-8">
      {/* Puntuaciones Académicas */}
      <div className="mb-8 p-6 bg-blue-50/50 rounded-xl border-l-4 border-blue-400">
        <h2 className="text-2xl font-bold text-blue-800 mb-6 flex items-center gap-3">
          📚 Puntuaciones Académicas
        </h2>
        
        <div className="grid md:grid-cols-2 gap-6">
          <div>
            <label htmlFor="reading_score" className="block text-sm font-semibold text-blue-700 mb-2">
              Puntuación de Lectura
            </label>
            <input
              type="number"
              id="reading_score"
              value={formData.reading_score !== undefined && formData.reading_score !== null ? formData.reading_score : ''}
              onChange={(e) => handleInputChange('reading_score', e.target.value === '' ? undefined : parseFloat(e.target.value))}
              min="0"
              max="100"
              step="0.1"
              className={`w-full px-4 py-3 border rounded-lg focus:ring-2 focus:ring-blue-400 focus:border-transparent transition-all bg-white text-gray-800 ${
                errors.reading_score !== undefined ? 'border-red-400' : 'border-blue-200'
              }`}
              placeholder="0-100"
            />
            {errors.reading_score !== undefined && (
              <p className="text-red-500 text-sm mt-1">
                {errors.reading_score === 0 ? 'La puntuación de lectura es obligatoria' : 'La puntuación debe estar entre 0 y 100'}
              </p>
            )}
            <p className="text-blue-600 text-sm mt-1">Valor entre 0 y 100</p>
          </div>

          <div>
            <label htmlFor="writing_score" className="block text-sm font-semibold text-blue-700 mb-2">
              Puntuación de Escritura
            </label>
            <input
              type="number"
              id="writing_score"
              value={formData.writing_score !== undefined && formData.writing_score !== null ? formData.writing_score : ''}
              onChange={(e) => handleInputChange('writing_score', e.target.value === '' ? undefined : parseFloat(e.target.value))}
              min="0"
              max="100"
              step="0.1"
              className={`w-full px-4 py-3 border rounded-lg focus:ring-2 focus:ring-blue-400 focus:border-transparent transition-all bg-white text-gray-800 ${
                errors.writing_score !== undefined ? 'border-red-400' : 'border-blue-200'
              }`}
              placeholder="0-100"
            />
            {errors.writing_score !== undefined && (
              <p className="text-red-500 text-sm mt-1">
                {errors.writing_score === 0 ? 'La puntuación de escritura es obligatoria' : 'La puntuación debe estar entre 0 y 100'}
              </p>
            )}
            <p className="text-blue-600 text-sm mt-1">Valor entre 0 y 100</p>
          </div>
        </div>
      </div>

      {/* Información Demográfica */}
      <div className="mb-8 p-6 bg-teal-50/50 rounded-xl border-l-4 border-teal-400">
        <h2 className="text-2xl font-bold text-teal-800 mb-6 flex items-center gap-3">
          👥 Información Demográfica
        </h2>
        
        <div className="grid md:grid-cols-3 gap-6">
          <div>
            <label htmlFor="lunch" className="block text-sm font-semibold text-teal-700 mb-2">
              Tipo de Almuerzo
            </label>
            <select
              id="lunch"
              value={formData.lunch}
              onChange={(e) => handleInputChange('lunch', parseInt(e.target.value))}
              className={`w-full px-4 py-3 border rounded-lg focus:ring-2 focus:ring-teal-400 focus:border-transparent transition-all bg-white text-gray-800 ${
                errors.lunch !== undefined ? 'border-red-400' : 'border-teal-200'
              }`}
            >
              <option value={1} className="text-gray-800 bg-white">Estándar</option>
              <option value={0} className="text-gray-800 bg-white">Gratuito/Reducido</option>
            </select>
            {errors.lunch !== undefined && (
              <p className="text-red-500 text-sm mt-1">{errors.lunch}</p>
            )}
          </div>

          <div>
            <label htmlFor="race_ethnicity_group_E" className="block text-sm font-semibold text-teal-700 mb-2">
              Grupo Étnico E
            </label>
            <select
              id="race_ethnicity_group_E"
              value={formData.race_ethnicity_group_E}
              onChange={(e) => handleInputChange('race_ethnicity_group_E', parseInt(e.target.value))}
              className={`w-full px-4 py-3 border rounded-lg focus:ring-2 focus:ring-teal-400 focus:border-transparent transition-all bg-white text-gray-800 ${
                errors.race_ethnicity_group_E !== undefined ? 'border-red-400' : 'border-teal-200'
              }`}
            >              
              <option value={0} className="text-gray-800 bg-white">No</option>
              <option value={1} className="text-gray-800 bg-white">Si</option>
            </select>
            {errors.race_ethnicity_group_E !== undefined && (
              <p className="text-red-500 text-sm mt-1">{errors.race_ethnicity_group_E}</p>
            )}
          </div>

          <div>
            <label htmlFor="gender" className="block text-sm font-semibold text-teal-700 mb-2">
              Género
            </label>
            <select
              id="gender"
              value={formData.gender}
              onChange={(e) => handleInputChange('gender', parseInt(e.target.value))}
              className={`w-full px-4 py-3 border rounded-lg focus:ring-2 focus:ring-teal-400 focus:border-transparent transition-all bg-white text-gray-800 ${
                errors.gender !== undefined ? 'border-red-400' : 'border-teal-200'
              }`}
            >
              <option value={0} className="text-gray-800 bg-white">Femenino</option>
              <option value={1} className="text-gray-800 bg-white">Masculino</option>
            </select>
            {errors.gender !== undefined && (
              <p className="text-red-500 text-sm mt-1">{errors.gender}</p>
            )}
          </div>
        </div>
      </div>

      {/* Información Educativa */}
      <div className="mb-8 p-6 bg-indigo-50/50 rounded-xl border-l-4 border-indigo-400">
        <h2 className="text-2xl font-bold text-indigo-800 mb-6 flex items-center gap-3">
          🎓 Información Educativa
        </h2>
        
        <div className="grid md:grid-cols-2 gap-6">
          <div>
            <label htmlFor="test_preparation_course" className="block text-sm font-semibold text-indigo-700 mb-2">
              Curso de Preparación
            </label>
            <select
              id="test_preparation_course"
              value={formData.test_preparation_course}
              onChange={(e) => handleInputChange('test_preparation_course', parseInt(e.target.value))}
              className={`w-full px-4 py-3 border rounded-lg focus:ring-2 focus:ring-indigo-400 focus:border-transparent transition-all bg-white text-gray-800 ${
                errors.test_preparation_course !== undefined ? 'border-red-400' : 'border-indigo-200'
              }`}
            >
              <option value={0} className="text-gray-800 bg-white">No</option>
              <option value={1} className="text-gray-800 bg-white">Si</option>
            </select>
            {errors.test_preparation_course !== undefined && (
              <p className="text-red-500 text-sm mt-1">{errors.test_preparation_course}</p>
            )}
          </div>

          <div>
            <label htmlFor="parental_level_of_education_high_school" className="block text-sm font-semibold text-indigo-700 mb-2">
              Nivel Educativo de los Padres Secundaria
            </label>
            <select
              id="parental_level_of_education_high_school"
              value={formData.parental_level_of_education_high_school}
              onChange={(e) => handleInputChange('parental_level_of_education_high_school', parseInt(e.target.value))}
              className={`w-full px-4 py-3 border rounded-lg focus:ring-2 focus:ring-indigo-400 focus:border-transparent transition-all bg-white text-gray-800 ${
                errors.parental_level_of_education_high_school !== undefined ? 'border-red-400' : 'border-indigo-200'
              }`}
            >             
              <option value={0} className="text-gray-800 bg-white">Otros títulos</option>
              <option value={1} className="text-gray-800 bg-white">Solo secundaria completa</option>
            </select>
            {errors.parental_level_of_education_high_school !== undefined && (
              <p className="text-red-500 text-sm mt-1">{errors.parental_level_of_education_high_school}</p>
            )}
          </div>
        </div>
      </div>

      {/* Botones de acción */}
      <div className="flex flex-col sm:flex-row gap-4 justify-center">
        <button
          type="submit"
          className="px-8 py-4 bg-gradient-to-r from-blue-500 to-indigo-600 text-white font-semibold rounded-lg hover:from-blue-600 hover:to-indigo-700 transform hover:scale-105 transition-all duration-200 shadow-lg"
        >
          📤 Enviar Datos
        </button>
        <button
          type="button"
          onClick={handleReset}
          className="px-8 py-4 bg-slate-400 text-white font-semibold rounded-lg hover:bg-slate-500 transform hover:scale-105 transition-all duration-200 shadow-lg"
        >
          🔄 Limpiar Formulario
        </button>
      </div>
    </form>
  );
}
