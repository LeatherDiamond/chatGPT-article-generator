# Navigation
* ***[Description](#description)***
* ***[How to start?](#how-to-start)***
* ***[Why should you try it?](#why-should-you-try-it)***
* ***[License](#license)***

# Description

This versatile script harnesses the power of ChatGPT to enhance your creative projects in two dynamic ways. Upon execution, you can choose between generating descriptions or images based on your specific needs. Let's explore the script's capabilities:

***Generating Descriptions:***

The script excels at content ideation. It generates five captivating titles and corresponding agendas, setting the stage for your creative endeavors. Once you've got your structure in place, the script crafts well-structured paragraphs that align with each agenda item. The magic doesn't stop there — results are automatically saved in an HTML file in the script's directory, ensuring easy access and organization.

***Generating Images:***

Adapting to visual projects, the script can fetch images based on your input. With a simple query, it connects to image repositories, retrieving images that match your concept. Whether you're designing presentations, blog posts, or social media content, this feature adds a visually appealing dimension to your work. Results are automatically saved in the script's directory.

# How to start?

**1. Clone current repository on your local machine:**
```
git clone https://github.com/LeatherDiamond/book_service.git
```

**2. Create and activate virtual environment on your machine:**
```
python -m venv env
.\env\Scripts\activate
```

**3. Install all requirements from "requirements.txt".**
```
pip install -r requirements.txt
```

**4. Provide `API_KEY` variable in `.env` file in the directory where the script is located.**

> You can generate API keys in the OpenAI web interface. See the [link](https://platform.openai.com/account/api-keys) for details.

**5. Run the script, choose the option of generating content, enjoy the power of ChatGPT.** 


# Why should you try it?

1. ***Effortless Content Ideation:*** With the script, generating content ideas becomes a breeze. It assists in brainstorming by automatically generating titles and agendas that serve as starting points for your creative projects.

2. ***Structured Content Creation:*** The script streamlines the content creation process by suggesting titles and agendas, while also recording generated paragraphs in a structured manner. This guarantees your final output is organized and coherent.

3. ***Time-Saving:*** Save hours by automating brainstorming, outlining, and content saving. The script significantly reduces the time invested in content preparation while maintaining high quality.

4. ***Diverse Applications:*** Suited for writers, presenters, and content creators, the script caters to various needs. It's perfect for generating blog post ideas, crafting presentation outlines, or creating engaging snippets for social media.

5. ***Harnessing GPT-3.5:*** Leveraging GPT-3.5's language capabilities, the script produces human-like text adapted to your context. Content is aligned with your intended style and tone, adding authenticity to your work.

6. ***Customizability:*** Tailor the script to your requirements. Easily modify parameters such as the number of titles, length of paragraphs, image size to match your preferences. This customization empowers you to fine-tune generated content to fit your project perfectly.

7. ***Image Generation:*** Take your creativity further with the ability to generate images based on your queries. The script fetches visuals that align with your ideas and saves them to the root directory, adding a visual dimension to your content.

Experience the convenience, efficiency, and accessibility of automated content generation. Try out this script and witness how it transforms your content creation workflow. Bid farewell to writer's block and welcome an endless stream of ideas, structured content, and visuals, all neatly saved in separate files alongside your script.

# License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/LeatherDiamond/chatGPT-article-generator/blob/main/LICENSE) file for details.
