import React, { useState } from 'react';
import axios from 'axios';

function GeneratedImageForm() {
  const [description, setDescription] = useState('');
  const [fileDownloadUrl, setFileDownloadUrl] = useState('');
  const [imageSrc, setImageSrc] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const response = await axios.post('http://localhost:8000/response/generated-images/', { description }, { responseType: 'arraybuffer' });
      const blob = new Blob([response.data], { type: 'image/png' });
      const imageUrl = URL.createObjectURL(blob);
      setImageSrc(imageUrl);
      setFileDownloadUrl(imageUrl);
    } catch (error) {
      console.error('Ошибка при создании генерированного изображения:', error);
    }
  };

  return (
    <div>
      <h2>Создать генерированное изображение</h2>
      <form onSubmit={handleSubmit}>
        <div>
          <label>Описание:</label>
          <input type="text" value={description} onChange={(e) => setDescription(e.target.value)} />
        </div>
        <button type="submit">Создать изображение</button>
      </form>
      {imageSrc && (
        <div>
          <p>Отобразить созданное изображение:</p>
          <img src={imageSrc} alt="Созданное изображение" />
        </div>
      )}
      {fileDownloadUrl && (
        <div>
          <p>Скачать созданное изображение: <a href={fileDownloadUrl} download>Скачать</a></p>
        </div>
      )}
    </div>
  );
}

export default GeneratedImageForm;