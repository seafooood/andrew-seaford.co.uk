// @ts-check
// `@type` JSDoc annotations allow editor autocompletion and type checking
// (when paired with `@ts-check`).
// There are various equivalent ways to declare your Docusaurus config.
// See: https://docusaurus.io/docs/api/docusaurus-config

import {themes as prismThemes} from 'prism-react-renderer';

// This runs in Node.js - Don't use client-side code here (browser APIs, JSX...)

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: 'My Site',
  tagline: 'Dinosaurs are cool',
  favicon: 'img/favicon.ico',

  // Future flags, see https://docusaurus.io/docs/api/docusaurus-config#future
  future: {
    v4: true, // Improve compatibility with the upcoming Docusaurus v4
  },

  // Set the production url of your site here
  url: 'https://your-docusaurus-site.example.com',
  // Set the /<baseUrl>/ pathname under which your site is served
  // For GitHub pages deployment, it is often '/<projectName>/'
  baseUrl: '/',

  // GitHub pages deployment config.
  // If you aren't using GitHub pages, you don't need these.
  organizationName: 'facebook', // Usually your GitHub org/user name.
  projectName: 'docusaurus', // Usually your repo name.

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
          editUrl:
            'https://github.com/facebook/docusaurus/tree/main/packages/create-docusaurus/templates/shared/',
        },
        blog: {
          path: './blog', // Make sure this is correct for your blog content
          routeBasePath: '/', // Set blog as homepage
          showReadingTime: true,
          feedOptions: {
            type: ['rss', 'atom'],
            xslt: true,
          },
          // Please change this to your repo.
          // Remove this to remove the "edit this page" links.
          editUrl:
            'https://github.com/facebook/docusaurus/tree/main/packages/create-docusaurus/templates/shared/',
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
      '@docusaurus/plugin-client-redirects',
      {
        redirects: [
          // If you have any specific redirects, add them here.
          // For example:
          // {
          //   to: '/docs/new-doc-path',
          //   from: '/old-wordpress-path',
          // },
        ],
        createRedirects: function (path) {
          // This function attempts to create redirects for old WordPress-style slugs.
          // It assumes old WordPress URLs were structured as /<slug>/
          // and Docusaurus doc paths can end with a slug, retaining their folder structure.
          const docMatch = path.match(/\/docs\/(.+?)\/([^\/]+)$/);
          if (docMatch) {
            const newSlug = docMatch[2]; // e.g., "3d-printed-toothbrush-holder"
            // Assuming old WordPress paths were /slug/
            const oldPath = `/${newSlug}/`;
            return oldPath;
          }
          return undefined;
        },
      },
    ],
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
      // Replace with your project's social card
      image: 'img/seaford-icon.jpg',
      colorMode: {
        respectPrefersColorScheme: true,
      },
      navbar: {
        title: 'My Site',
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
          },
          {
            href: 'https://github.com/facebook/docusaurus',
            label: 'GitHub',
            position: 'right',
          },
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
                label: 'GitHub',
                href: 'https://github.com/andrew-seaford',
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
