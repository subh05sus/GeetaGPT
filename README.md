# GeetaGPT

GeetaGPT is a chatbot built with Flask that embodies the persona of Lord Krishna, possessing extensive knowledge from Shrimadvagwat Geeta. The bot is powered by the OpenAI GPT-3.5 model, capable of answering life problems, providing advice, and offering motivation.

## Features

- **Divine Wisdom:** Acts as a replica of Lord Krishna, answering questions and offering advice based on the teachings of Shrimadvagwat Geeta.
- **Life Guidance:** Provides insightful responses to life problems and challenges.
- **Motivational Chat:** Offers motivation and uplifting messages for users feeling low.

## Usage Instructions

1. **Setup:**
   - Clone the repository: `git clone https://github.com/yourusername/GeetaGPT.git`
   - Navigate to the project directory: `cd GeetaGPT`

2. **Configuration:**
   - Create a `.env` file in the root of the project.
   - Add your OpenAI API key to the `.env` file: `API_KEY=your_openai_api_key`.
   - Update `main.py` to load the API key from the environment: `OpenAIAPI = os.getenv("API_KEY")`.

3. **Environment Setup:**
   - Create a virtual environment: `python -m venv venv`
   - Activate the virtual environment:
     - On Windows: `venv\Scripts\activate`
     - On Unix or MacOS: `source venv/bin/activate`

4. **Install Dependencies:**
   - Install required packages: `pip install -r requirements.txt`

5. **Run the Application:**
   - Start the Flask server: `python main.py`
   - Access the application in your browser: [http://localhost:80/](http://localhost:80/)

## Screenshots

![Main Page](https://user-images.githubusercontent.com/116567041/229670073-5e64b92c-56fe-4732-b701-5e0bd0e75e05.png)
![Other](https://user-images.githubusercontent.com/116567041/229670093-0daa5520-8164-46e9-8e4c-0f7bf50d8e4a.png)

## Contribution Guidelines

Feel free to contribute! Follow these steps:
1. Fork the repository.
2. Create a new branch: `git checkout -b feature/your-feature`.
3. Commit your changes: `git commit -m "Add your feature"`.
4. Push to the branch: `git push origin feature/your-feature`.
5. Submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments

Special thanks to [OpenAI](https://platform.openai.com/) for providing the powerful GPT-3.5 model.

---

This project is maintained by [Your Name]. Feel free to reach out with any questions or suggestions!
