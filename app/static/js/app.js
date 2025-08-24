// JavaScript básico para la aplicación Flask
document.addEventListener('DOMContentLoaded', function() {
    console.log('Aplicación Flask cargada correctamente');
    
    // Función para mostrar mensajes de éxito
    function showSuccess(message) {
        const resultDiv = document.getElementById('result');
        if (resultDiv) {
            resultDiv.innerHTML = `<div class="result success">${message}</div>`;
        }
    }
    
    // Función para mostrar mensajes de error
    function showError(message) {
        const resultDiv = document.getElementById('result');
        if (resultDiv) {
            resultDiv.innerHTML = `<div class="result error">${message}</div>`;
        }
    }
    
    // Función para validar formulario
    function validateForm() {
        const requiredFields = document.querySelectorAll('[required]');
        let isValid = true;
        
        requiredFields.forEach(field => {
            if (!field.value || field.value.trim() === '' || field.value === '') {
                field.style.borderColor = 'red';
                isValid = false;
            } else {
                field.style.borderColor = '#ddd';
            }
        });
        
        return isValid;
    }
    
    // Función para manejar el envío del formulario
    function handleFormSubmit(e) {
        e.preventDefault();
        
        if (!validateForm()) {
            showError('⚠️ Por favor, completa todos los campos requeridos');
            return;
        }
        
        // Recopilar datos del formulario
        const formData = new FormData(e.target);
        const data = {};
        
        // Convertir FormData a objeto
        for (let [key, value] of formData.entries()) {
            // Solo procesar valores que no estén vacíos
            if (value && value.trim() !== '') {
                // Convertir valores string a números donde sea necesario
                if (['reading_score', 'writing_score'].includes(key)) {
                    data[key] = parseFloat(value);
                } else if (['gender', 'lunch', 'test_preparation_course', 'race_ethnicity_group_E', 'parental_level_of_education_high_school'].includes(key)) {
                    data[key] = parseInt(value);
                } else {
                    data[key] = value;
                }
            }
        }
        
        // Mostrar indicador de carga
        showSuccess('🔄 Procesando predicción...');
        
        // Enviar datos al servidor
        fetch('/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data)
        })
        .then(response => response.json())
        .then(result => {
            if (result.error) {
                showError(`❌ Error: ${result.error}`);
            } else {
                showSuccess(`🎯 ¡Predicción exitosa! Calificación matemática: ${result.math_score_prediction}/100`);
            }
        })
        .catch(error => {
            console.error('Error:', error);
            showError('🌐 Error de conexión con el servidor');
        });
    }
    
    // Agregar manejo del formulario
    const form = document.querySelector('form');
    if (form) {
        form.addEventListener('submit', handleFormSubmit);
    }
});
