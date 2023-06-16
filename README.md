Simpler reproduction of the famous (and creepy) [https://fortune.com/2023/05/09/snapchat-influencer-launches-carynai-virtual-girlfriend-bot-openai-gpt4/ ai-girfriend](URL).
Capabilities:
- Pretend to be your girlfriend.
- Knows your name.
- Can accept text or audio input.
- Reply with audio only to your messages.
- Have paying users - 1$/min (test or real payments with Stripe)

To Run:
1 - Clone the repo 
2 - Run pip install -r requirements.txt
3 - Create a telegram bot and get the token.
4 - Create a MongoDB (free tier) database. Name it as you want, create 2 collections named: users, message_history. Enable network access from all IPs.
5 - Get all API keys (Openai, ElevenLabs, MongoDB, StripeTest) and write them on the .env template file. Rename the file to .env.
6 - run python3 telegram_bot.py

Note: the user has to pay and then he can chat with the bot.

System overview
Once User pays he gets registered as a customer in the DB along with his expiration time.
When he chats, a langchain chain using OpenAI responds as his girfriend. 
The text and the model response are saved in the DB and used as history chat in the next messages.
The model response goes into Eleven Labs text-2-speech and the audio is sent to the user as response.
 
