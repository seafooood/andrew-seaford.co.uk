import React, { useEffect, useRef } from 'react';

const AdComponent = () => {
  const adRef = useRef(null);

  useEffect(() => {
    if (adRef.current) {
      const script = document.createElement('script');
      script.innerHTML = `
        atOptions = {
          'key' : 'b8987abc4828c7a6fbe28bd3dc48c261',
          'format' : 'iframe',
          'height' : 600,
          'width' : 160,
          'params' : {}
        };
      `;
      adRef.current.appendChild(script);

      const script2 = document.createElement('script');
      script2.src = 'https://www.highperformanceformat.com/b8987abc4828c7a6fbe28bd3dc48c261/invoke.js';
      script2.async = true;
      adRef.current.appendChild(script2);

      return () => {
        if (adRef.current) {
          adRef.current.removeChild(script);
          adRef.current.removeChild(script2);
        }
      };
    }
  }, []);

  return  <fieldset>
  <legend>Adverts</legend>
  <div ref={adRef}></div>
</fieldset>
  
};

export default AdComponent;
