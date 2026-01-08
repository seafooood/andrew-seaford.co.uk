const fs = require('fs');
const path = require('path');

function toTitleCase(str) {
  return str.replace(/-/g, ' ').split(' ').map(word => word.charAt(0).toUpperCase() + word.slice(1)).join(' ');
}

module.exports = function (context, options) {
  return {
    name: 'tutorial-data-plugin',
    async loadContent() {
      const docsPath = path.resolve(context.siteDir, 'docs');
      const categories = fs.readdirSync(docsPath, { withFileTypes: true })
        .filter(dirent => dirent.isDirectory())
        .map(dirent => dirent.name);

      const tutorialData = categories.map(category => {
        const categoryPath = path.join(docsPath, category);
        const tutorials = fs.readdirSync(categoryPath, { withFileTypes: true })
          .filter(dirent => dirent.isDirectory())
          .map(dirent => dirent.name);
        
        return {
          name: toTitleCase(category),
          pathName: category,
          tutorials: tutorials,
        };
      });

      return tutorialData;
    },
    async contentLoaded({content, actions}) {
      const {setGlobalData} = actions;
      setGlobalData({tutorialData: content});
    },
  };
};
