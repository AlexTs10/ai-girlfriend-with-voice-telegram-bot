# AI-Girlfriend Bot 🤖❤️

![AI-Girlfriend Banner](banner_image_url_here)

AI-Girlfriend Bot is a simple application based on OpenAI GPT-4 that simulates a conversation with an AI-powered virtual girlfriend. This is a simpler reproduction of the famous (and somewhat creepy) [AI Girlfriend featured on Fortune](https://fortune.com/2023/05/09/snapchat-influencer-launches-carynai-virtual-girlfriend-bot-openai-gpt4/).

## Features 🌟
- 🧡 Pretends to be your girlfriend
- 📛 Knows your name
- 🎙️ Accepts text or audio input
- 🔈 Replies with audio messages
- 💳 Supports payments through Stripe ($1/min)

## Quick Start 🚀

### Prerequisites
- Python 3
- A Telegram bot token
- A MongoDB database
- API keys from OpenAI, ElevenLabs, MongoDB, and Stripe

### Setup & Running
1. Clone the repository:
2. Navigate to the cloned directory and install the required Python packages: pip install -r requirements.txt
3. Create a Telegram bot and obtain the bot token.
4. Set up a MongoDB database (you can use the free tier). Name it as you wish and create two collections: `users`, and `message_history`. Ensure network access is enabled for all IPs.
5. Obtain API keys from OpenAI, ElevenLabs, MongoDB, and Stripe (for testing) and populate them in the provided `.env` template file. After filling in the keys, rename the file to `.env`.
6. Run the bot: python3 telegram_bot.py


## How it Works 🛠️

1. **Payment & Registration:** Users need to make a payment to interact with the bot. Upon payment, the user gets registered as a customer in the database with an expiration time.

2. **Conversing with the Bot:** When a user sends a message, a language model from OpenAI responds as the virtual girlfriend.

3. **Saving the Conversation:** The user's message and the model's response are saved in the MongoDB database and can be used as chat history for subsequent messages.

4. **Text-to-Speech Conversion:** The model's response is converted into audio using Eleven Labs' text-to-speech service.

5. **Sending Audio Response:** The audio is sent to the user as a response through Telegram.

## Contributing 🤝
We welcome contributions! Please read our contributing guide for details on how to get started.

## License 📄
This project is licensed under the MIT License - see the LICENSE.md file for details.

## Acknowledgements 🙏
- OpenAI for GPT-4
- Eleven Labs for text-to-speech service
- Telegram for messaging platform
- MongoDB for database services
- Stripe for payment services
