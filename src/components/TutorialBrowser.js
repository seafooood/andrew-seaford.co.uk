import React, { useState } from 'react';
import Link from '@docusaurus/Link';
import styles from './TutorialBrowser.module.css';

const tutorialData = [
    { name: 'Docker', pathName: 'docker', tutorials: [
        "A Guide to Removing Unused Docker Images on Ubuntu",
        "containerize an inno installed application",
        "containerize net framework 4 8 console application",
        "How To Automatically Start A Docker Container",
        "How To Avoid Using sudo with Docker",
        "How To Containerize A Python Flask Application",
        "How To Create A Multi Layer Docker Compose",
        "installing docker",
        "Monitoring Docker Statistics",
        "Troubleshooting KeyError ContainerConfig",
        "troubleshooting-image-in-use",
    ]},
    { name: 'Flameshot', pathName: 'flameshot', tutorials: ["How To Install Flameshot"] },
    { name: 'FreeCAD', pathName: 'freecad', tutorials: [
        "3d-printed-toothbrush-holder",
        "Darts Stand",
        "FischertechnikBlockSmall",
        "Getting Started With FreeCAD Spreadsheets and Parametric Design",
        "How to Create a Custom 3D-Printed Christmas Stamp with FreeCAD",
        "Mico Generator",
        "Oversized \"TOILET\" Keyring for Cafes & Restaurants (The Giant Spoon)",
        "Oversized-TOILET-Keyring-for-Workshops-Garages",
        "Wire Stripper",
    ]},
    { name: 'Gemini', pathName: 'gemini', tutorials: ["Configuring Gemini Permissions", "How To Install Gemini Cli"] },
    { name: 'GitHub', pathName: 'github', tutorials: ["How to Set Up GitHub Actions to Automatically Run npm test", "How to Set Up GitHub Actions to Automatically Run Pytests"] },
    { name: 'Hugo', pathName: 'hugo', tutorials: ["Installing Hugo on Ubuntu"] },
    { name: 'Inno', pathName: 'inno', tutorials: [
        "automatically target exe version inno",
        "check dotnet framework installed inno setup",
        "check program exists installing inno",
        "create empty folders inno",
        "custom inno theme",
        "free disk space inno",
        "installing inno installer",
    ]},
    { name: 'Langflow', pathName: 'langflow', tutorials: [
        "How To Chat With Langflow From A Python Script",
        "How To Enable Logging In Langflow",
        "How To Install Langflow on Ubuntu Using Docker",
        "How To Install Langflow on Ubuntu Without Docker",
    ]},
    { name: 'Milling Machine CNC', pathName: 'milling machine cnc', tutorials: [
        "axis drops completing job",
        "marlinfw homing direction",
        "reporting endstop status",
        "simple box code",
    ]},
    { name: 'MySQL', pathName: 'mysql', tutorials: ["Installing MySQL with phpMyAdmin"] },
    { name: 'n8n', pathName: 'n8n', tutorials: [
        "Code Node - JsProxy to Python",
        "Code Node - Read Text File",
        "How To Install n8n with Langchain.js",
    ]},
    { name: 'OpenCV', pathName: 'opencv', tutorials: [
        "detecting dominant points image opencv",
        "drawing simple shapes opencv",
        "flood fill opencv",
        "gaussian image smoothing opencv",
        "image contour detection display opencv",
        "opencv csharp wpf application",
        "opencv world",
        "splitting multichannel images rgb opencv",
        "threshold image opencv",
        "wood cells",
    ]},
    { name: 'Oracle', pathName: 'oracle', tutorials: ["backup oracle database", "oracle insert date"] },
    { name: 'Pinecone', pathName: 'pinecone', tutorials: [
        "How To Find Index Dimensions",
        "How To Install Pinecone",
        "How To List Pinecone Vectors",
        "How To Upload Test Data To Pinecone",
    ]},
    { name: 'PostgreSQL', pathName: 'postgresql', tutorials: [
        "How To Perform a Vector Search in A Postgres Database using pgvector",
        "install",
        "Install pgvector on Ubuntu with PostgreSQL 14",
    ]},
    { name: 'Programming C Sharp', pathName: 'programming c sharp', tutorials: [
        "adding days datetime csharp",
        "c open file dialog",
        "create arraylist",
        "create autocompleting textbox c",
        "csharp class properties",
        "csharp type checking statement",
        "data validation exceptions csharp",
        "enumerations with tryparse csharp",
        "equal c",
        "explicit conversion string integer csharp",
        "how to use extension methods in c",
        "reading file csharp",
        "recursive delete files folders c",
        "simple cshar linq",
        "simple csharp stringbuilder",
        "simple write file csharp",
        "string formating csharp",
        "web page content string c",
    ]},
    { name: 'Programming Javascript', pathName: 'programming javascript', tutorials: [
        "creating a restfull server using nextjs",
        "how to build a static page that refreshes every 60 seconds using nextjs",
        "how to create a combobox react component with unit tests",
        "how to create a next js app from scratch",
        "how to create a react component that returns a promise with unit tests",
        "how to handle server side api routes in react",
        "how to mock a function and confirm the function was called",
        "how to mock a function that returns a value",
    ]},
    { name: 'Programming JQuery', pathName: 'programming jquery', tutorials: ["Popup"] },
    { name: 'Programming PHP', pathName: 'programming php', tutorials: [
        "convert date time utc",
        "sound buttons",
        "split php",
        "urltonvp",
    ]},
    { name: 'Programming Python', pathName: 'programming python', tutorials: [
        "django", "dotenv", "flask", "gemini", "general", "gpt4all",
        "importlib", "logging", "pil", "pip", "regx", "sqlite3",
        "sqllite", "tkinter", "venv",
    ]},
    { name: 'Raspberry Pi', pathName: 'raspberry pi', tutorials: [
        "configuring static ip address raspberry pi",
        "moving forwards",
        "ps3 controller",
        "stepper motor control service",
    ]},
    { name: 'Ubuntu', pathName: 'ubuntu', tutorials: [
        "Apt vs Apt-get",
        "Disk Cleanup Ubuntu",
        "How To Assign A Static Ip Address in Ubuntu",
        "How To Change Hostname In Ubuntu",
        "How to Customize Your Bash Prompt On Ubuntu",
        "ubuntu 12 4 enable ssh service",
    ]},
    { name: 'VirtualBox', pathName: 'virtualbox', tutorials: [
        "Attaching-a-DVD-ISO-Image-in-VirtualBox",
        "Check VM Status",
        "Cloning a VirtualBox VM via Ubuntu Terminal",
        "export virtualbox virtual machines",
        "Finding VM Disk Location",
        "Installing VirtualBox Guest Additions in Ubuntu Guest Virtual Machine",
        "Resize the VirtualBox Disk (.vdi)",
        "Taking a Virtual Machine Snapshot via Ubuntu Terminal",
    ]},
    { name: 'VS Code', pathName: 'vs code', tutorials: ["How To Force VS Code To Open Files In A New Tab"] },
    { name: 'Windows CMD', pathName: 'windows cmd', tutorials: ["create m3u playlist from directory list", "How To Hide Address In Prompt"] },
    { name: 'WooCommerce', pathName: 'woocommerce', tutorials: ["how to find woocommerce consumer key and secret"] },
];

const TutorialBrowser = () => {
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
