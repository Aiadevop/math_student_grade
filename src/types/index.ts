export interface FormData {
  reading_score: number;
  writing_score: number;
  lunch: number;
  race_ethnicity_group_E: number;
  test_preparation_course: number;
  gender: number;
  parental_level_of_education_high_school: number;
}

export interface FormErrors {
  reading_score?: number;
  writing_score?: number;
  lunch?: number;
  race_ethnicity_group_E?: number;
  test_preparation_course?: number;
  gender?: number;
  parental_level_of_education_high_school?: number;
}

export interface PerformanceLevel {
  level: string;
  color: string;
  bg: string;
}

export const FIELD_NAMES = {
  reading_score: '📖 Puntuación de Lectura',
  writing_score: '✍️ Puntuación de Escritura',
  lunch: '🍽️ Tipo de Almuerzo',
  race_ethnicity_group_E: '👥 Grupo Étnico E',
  test_preparation_course: '📚 Curso de Preparación',
  gender: '👤 Género',
  parental_level_of_education_high_school: '🎓 Nivel Educativo de los Padres Secundaria'
} as const;

export const LUNCH_OPTIONS = [
  { value: 1, label: 'Estándar' },
  { value: 0, label: 'Gratuito/Reducido' }
] as const;

export const ETHNICITY_OPTIONS = [
  { value: 0, label: 'No' },
  { value: 1, label: 'Si' }
] as const;

export const GENDER_OPTIONS = [
  { value: 0, label: 'Femenino' },
  { value: 1, label: 'Masculino' }
] as const;

export const PREPARATION_OPTIONS = [
  { value: 0, label: 'No' },
  { value: 1, label: 'Si' }
] as const;

export const EDUCATION_OPTIONS = [
  { value: 0, label: 'Otros títulos' },
  { value: 1, label: 'Solo secundaria completa' }
] as const;
