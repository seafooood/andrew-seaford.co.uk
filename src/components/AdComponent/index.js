import React, { useEffect, useRef } from 'react';

const AdComponent = () => {
  const adRef = useRef(null);

  useEffect(() => {
    if (adRef.current) {
      const script = document.createElement('script');
      script.src = 'https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-3561429949247088';
      script.async = true;
      script.crossOrigin = 'anonymous';
      adRef.current.appendChild(script);

      return () => {
        if (adRef.current) {
          adRef.current.removeChild(script);
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
