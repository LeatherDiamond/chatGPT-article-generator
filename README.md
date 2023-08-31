# Navigation
* ***[Description](#description)***
* ***[Software versions](#software-versions)***
* ***[How to start?](#how-to-start)***
* ***[Using the API](#using-the-api)***
* ***[Code formatting and Quality checking tools](#code-formatting-and-quality-checking-tools)***
* ***[Frontend](#frontend)***
* ***[Why should you try it?](#why-should-you-try-it)***
* ***[License](#license)***

# Description

The backend repository is an integral part of the comprehensive creative project solution. It functions as the backend component of the system, providing the following key features:

***Description Generation:***

The backend system is optimized for content ideation. It generates several compelling titles and corresponding agendas, serving as a robust framework for your creative projects. Once the structure is defined, the backend system meticulously constructs well-organized paragraphs that align with each agenda item. Importantly, the results are automatically saved in an HTML file, ensuring easy access and efficient organization.

***Generating Images:***

In addition, the backend system seamlessly adapts to visual projects by retrieving images based on your input. Utilizing a straightforward query, it  retrieves images that precisely match your conceptual requirements. This feature is invaluable for enhancing presentations, blog posts, or social media content with visually captivating elements. As always, the results are automatically stored within the backend system's directory.

The backend repository forms the backbone of the creative project solution, offering powerful tools for content and image generation to enhance your creative endeavors.

# Software versions

- PYTHON: ***3.11.3***
- PIP: ***23.1.2***
- POETRY: ***1.5.1***
- DJANGO: ***4.2.1***
- DJANGO REST FRAMEWORK: ***3.14.0***
  
# How to start?

**1. Clone current repository on your local machine:**
```
git clone https://github.com/LeatherDiamond/book_service.git
```

**2. Activate virtual environment on your machine:**
```
poetry shell
```

**3. Install all the requirements for the project:**
```
poetry install
```

**4. Configure `.env` file by assigning values to the variables defined in `env.sample`**
> ###### NOTE:
> ***You can generate API keys in the OpenAI web interface. See the [link](https://platform.openai.com/account/api-keys) for details.***

**5. Run the project:** 
```
python manage.py runserver
```

After completing all the steps, the project will be launched and available at `http://localhost:8000/`.

# Using the API

The project provides full api documentation in the following endpoint: `api/docs/`. Make GET request to this endpoint to view the entire project's API schema.

# Code formatting and Quality checking tools

1. Run `poetry shell` to activate environment if it's not active yet;
2. Run `black . --check` to check if the code needs to be reformatted;
3. Run `black .` to reformat the code;
4. Run `flake8` to identify potential issues, such as syntax errors, code style violations, and other coding inconsistencies during the development process;

# Frontend

The frontend of the project is developed using React, a popular JavaScript library for building user interfaces. It resides in a separate repository, distinct from the backend. Leveraging the power of React's component-based architecture, the frontend provides a dynamic and responsive user experience.

Utilizing modern frontend technologies such as JSX (JavaScript XML), CSS-in-JS for styling, and various state management libraries, the React frontend seamlessly communicates with the backend through API calls. This interaction ensures efficient data exchange, enabling users to interact with the creative project solution effortlessly.

The frontend repository can be found by the following [link](https://github.com/LeatherDiamond/chatGPT-content-generator-Frontend), where you can explore the React codebase, UI components, and the integration with the backend API. This separation of concerns allows for easy maintenance, scalability, and the ability to evolve the user interface independently from the backend logic.

# Why should you try it?

1. ***Effortless Content Ideation:*** With the project, generating content ideas becomes a breeze. It assists in brainstorming by automatically generating titles and agendas that serve as starting points for your creative projects.

2. ***Structured Content Creation:*** The project streamlines the content creation process by suggesting titles and agendas, while also recording generated paragraphs in a structured manner. This guarantees your final output is organized and coherent.

3. ***Time-Saving:*** Save hours by automating brainstorming, outlining, and content saving. The project significantly reduces the time invested in content preparation while maintaining high quality.

4. ***Diverse Applications:*** Suited for writers, presenters, and content creators, the project caters to various needs. It's perfect for generating blog post ideas, crafting presentation outlines, or creating engaging snippets for social media.

5. ***Harnessing GPT-3.5:*** Leveraging GPT-3.5's language capabilities, the project produces human-like text adapted to your context. Content is aligned with your intended style and tone, adding authenticity to your work.

6. ***Customizability:*** Easily modify parameters such as the number of titles and items in agendas, length of paragraphs to match your preferences. This customization empowers you to fine-tune generated content to fit your project perfectly.

7. ***Image Generation:*** Take your creativity further with the ability to generate images based on your queries. The project fetches visuals that align with your ideas and saves them to the root directory, adding a visual dimension to your content.

Experience the convenience, efficiency, and accessibility of automated content generation. Try out this project and witness how it transforms your content creation workflow. Bid farewell to writer's block and welcome an endless stream of ideas, structured content, and visuals, all neatly saved in separate files alongside your project and always available for downloading from your browser.

# License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/LeatherDiamond/chatGPT-article-generator/blob/main/LICENSE) file for details.
