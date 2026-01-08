import React from 'react';
import Layout from '@theme-original/DocItem/Layout';
import AdComponent from '../../../components/AdComponent';

export default function LayoutWrapper(props) {
  return (
    <div style={{display: 'flex'}}>
      <div style={{flex: 1}}>
        <Layout {...props} />
      </div>
      <AdComponent />
    </div>
  );
}
