import React, { useState } from 'react';
import Link from '@docusaurus/Link';
import { usePluginData } from '@docusaurus/useGlobalData';
import styles from './TutorialBrowser.module.css';

const TutorialBrowser = () => {
  const { tutorialData } = usePluginData('tutorial-data-plugin');
  const [selectedCategory, setSelectedCategory] = useState(null);

  const handleCategoryClick = (category) => {
    if (selectedCategory && selectedCategory.name === category.name) {
      setSelectedCategory(null);
    } else {
      setSelectedCategory(category);
    }
  };

  return (
    <div className={styles.browser}>
      <div className={styles.categoryGrid}>
        {tutorialData.map((category) => (
          <div
            key={category.name}
            className={`${styles.categoryCard} ${selectedCategory && selectedCategory.name === category.name ? styles.selected : ''}`}
            onClick={() => handleCategoryClick(category)}
          >
            {category.name}
          </div>
        ))}
      </div>
      {selectedCategory && (
        <div className={styles.tutorialList}>
          <h2>{selectedCategory.name}</h2>
          <ul>
            {selectedCategory.tutorials.map((tutorial) => {
                const path = `/docs/${selectedCategory.pathName}/${tutorial}`;
                return (
                    <li key={tutorial}>
                        <Link to={path}>{tutorial}</Link>
                    </li>
                );
            })}
          </ul>
        </div>
      )}
    </div>
  );
};

export default TutorialBrowser;