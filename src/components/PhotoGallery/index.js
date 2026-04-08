import React from 'react';
import styles from './styles.module.css';

export default function PhotoGallery({ photos }) {
  return (
    <div className={styles.gallery}>
      {photos.map((photo, i) => (
        <div key={i} className={styles.photoCard}>
          <a href={photo.src} target="_blank" rel="noopener noreferrer">
            <img src={photo.src} alt={photo.alt} className={styles.thumbnail} />
          </a>
          <a href={photo.src} target="_blank" rel="noopener noreferrer" className={styles.caption}>
            {photo.alt}
          </a>
        </div>
      ))}
    </div>
  );
}
