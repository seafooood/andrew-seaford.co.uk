import React from 'react';
import BlogLayout from '@theme-original/BlogLayout';
import AdComponent from '../../components/AdComponent';

export default function BlogLayoutWrapper(props) {
  return (
    <BlogLayout {...props} toc={<AdComponent />} />
  );
}
