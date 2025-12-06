# About
A small proof of concept of an analytical system for moderation support. The model to classify messages for moderation was prepared [here](https://github.com/CatGamer7/Telegram-threats).

# Structure
The system consists of 4 services:
- Backend server that uses a language model to classify texts. Written with Python, drf and onnx;
- Telegram bot that listens for messages and calld backend server for inference, written with python-telegram-bot;
- Database that stores historical data of classified texts. Postgres was chosen;
- Frontend app with a dashboard, written in React.

# About author
CatGamer7 - Zaida Artur - Зайда Артур, студент группы 8ПМ52 НИ ТПУ
