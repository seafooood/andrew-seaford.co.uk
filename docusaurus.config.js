// @ts-check
// `@type` JSDoc annotations allow editor autocompletion and type checking
// (when paired with `@ts-check`).
// There are various equivalent ways to declare your Docusaurus config.
// See: https://docusaurus.io/docs/api/docusaurus-config

import {themes as prismThemes} from 'prism-react-renderer';

// This runs in Node.js - Don't use client-side code here (browser APIs, JSX...)

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: 'Andrew Seaford',
  tagline: 'Andrew Seaford\'s personal website and blog',
  favicon: 'img/favicon.ico',

  // Future flags, see https://docusaurus.io/docs/api/docusaurus-config#future
  future: {
    v4: true, // Improve compatibility with the upcoming Docusaurus v4
  },

  // Set the production url of your site here
  url: 'https://www.andrew-seaford.co.uk',
  trailingSlash: false,
  // Set the /<baseUrl>/ pathname under which your site is served
  // For GitHub pages deployment, it is often '/<projectName>/'
  baseUrl: '/',

  // GitHub pages deployment config.
  // If you aren't using GitHub pages, you don't need these.
  organizationName: 'seafooood', // Usually your GitHub org/user name.
  projectName: 'andrew-seaford.co.uk', // Usually your repo name.

  onBrokenLinks: 'throw',

  // Even if you don't use internationalization, you can use this field to set
  // useful metadata like html lang. For example, if your site is Chinese, you
  // may want to replace "en" with "zh-Hans".
  i18n: {
    defaultLocale: 'en',
    locales: ['en'],
  },

  presets: [
    [
      'classic',
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: {
          sidebarPath: './sidebars.js',
          // Please change this to your repo.
          // Remove this to remove the "edit this page" links.
        },
        blog: {
          path: './blog', // Make sure this is correct for your blog content
          routeBasePath: '/', // Set blog as homepage
          blogDescription: 'Technical tutorials and insights on Docker, Python, OpenCV, 3D printing, and robotics by Andrew Seaford.',
          showReadingTime: true,
          feedOptions: {
            type: ['rss', 'atom'],
            xslt: true,
          },
          // Please change this to your repo.
          // Remove this to remove the "edit this page" links.
          // Useful options to enforce blogging best practices
          onInlineTags: 'warn',
          onInlineAuthors: 'warn',
          onUntruncatedBlogPosts: 'warn',
        },
        theme: {
          customCss: './src/css/custom.css',
        },
      }),
    ],
  ],

  plugins: [
    './plugins/tutorial-data-plugin',
    [
      '@docusaurus/plugin-content-docs',
      {
        id: 'portfolio',
        path: 'portfolio',
        routeBasePath: 'portfolio',
        sidebarPath: './sidebarsPortfolio.js',
      },
    ],
    [
      '@docusaurus/plugin-content-docs',
      {
        id: 'shop',
        path: 'shop',
        routeBasePath: 'shop',
        sidebarPath: './sidebarsShop.js',
      },
    ],
  ],

  themeConfig:
    /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
    ({
      metadata: [
        {name: 'keywords', content: '3D printing, Programming, Robotics,opencv, docker, computer science, technical consultant, Raspberry Pi'},
        {name: 'description', content: 'Technical insights on 3D printing, Robotics, and software development by Andrew Seaford.'},
      ],
      // Replace with your project's social card
      image: 'img/seaford-icon.jpg',
      colorMode: {
        respectPrefersColorScheme: true,
      },
      navbar: {
        title: 'Andrew Seaford',
        logo: {
          alt: 'My Site Logo',
          src: 'img/logo.svg',
        },
        items: [
          {
            type: 'docSidebar',
            sidebarId: 'tutorialSidebar',
            position: 'left',
            label: 'Tutorials',
          },
          {
            type: 'doc',
            docId: 'index',
            docsPluginId: 'portfolio',
            position: 'left',
            label: 'Portfolio',
          },
          {
            type: 'doc',
            docId: 'index',
            docsPluginId: 'shop',
            position: 'left',
            label: 'Shop',
          }
        ],
      },
      footer: {
        style: 'dark',
        links: [
          {
            title: 'Docs',
            items: [
              {
                label: 'Tutorials',
                to: '/docs/intro',
              },
              {
                label: 'Portfolio',
                to: '/portfolio',
              },
              {
                label: 'Shop',
                to: '/shop',
              },
            ],
          },
          {
            title: 'Social',
            items: [
              {
                label: 'LinkedIn',
                href: 'https://www.linkedin.com/in/andrew-seaford/',
              },
              {
                label: 'GitHub',
                href: 'https://github.com/seafooood/',
              },
            ],
          },
        ],
        copyright: `Copyright © ${new Date().getFullYear()} Andrew Seaford. Built with Docusaurus.`,
      },
      prism: {
        theme: prismThemes.github,
        darkTheme: prismThemes.dracula,
      },
    }),
};

export default config;
