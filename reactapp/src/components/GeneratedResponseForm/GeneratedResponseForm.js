import React, { useState } from 'react';
import axios from 'axios';

function GeneratedResponseForm() {
  const [userInput, setUserInput] = useState('');
  const [numTitles, setNumTitles] = useState(5);
  const [numAgendas, setNumAgendas] = useState(5);
  const [numWords, setNumWords] = useState(250);

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const response = await axios.post('/response/generated-responses/', {
        user_input: userInput,
        num_titles: numTitles,
        num_agendas: numAgendas,
        num_symbols: numWords,
      });

      const fileAbsolutePath = response.data.file_path;
      // Здесь можно обработать файл, например, показать его пользователю.
    } catch (error) {
      console.error('Ошибка при создании генерированного ответа:', error);
    }
  };

  return (
    <div>
      <h2>Создать генерированный ответ</h2>
      <form onSubmit={handleSubmit}>
        <div>
          <label>Ваш запрос:</label>
          <input type="text" value={userInput} onChange={(e) => setUserInput(e.target.value)} />
        </div>
        {/* Добавьте остальные поля ввода */}
        <button type="submit">Создать ответ</button>
      </form>
    </div>
  );
}

export default GeneratedResponseForm;