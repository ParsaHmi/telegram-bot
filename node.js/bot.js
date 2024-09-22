const TelegramBot = require('node-telegram-bot-api');
const fastify = require('fastify')();
const TOKEN = 'YOUR-BOT-API'; //enter your bot API 

const bot = new TelegramBot(TOKEN, { polling: true });

const channelId = '@ID'; //Enter your channel ID

async function checkTimeLoop() {
  while (true) {
    const now = new Date();
    let hours = now.getHours();
    let minutes = now.getMinutes();

if (hours === minutes) {
  bot.sendMessage(channelId, `${hours}:${minutes}`).then(() => {
    console.log(` massage sent : ${hours}:${minutes}`);
  }).catch((error) => {
    console.error('there was an ERROR ! : ', error);
  });
} else {
    console.log('');
}
    await delay(50000); 
  }
}

function delay(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

checkTimeLoop();

bot.on('message', (msg) => {
  const chatId = msg.chat.id;
  const text = msg.text;
  const name = msg.username;

  bot.sendMessage(chatId, 'do not Text me !');
});

fastify.get('/', function (request, reply) {
  reply.send({ message: 'telegram bot is activate  ' });
});

fastify.listen(process.env.PORT || 3000, (err, address) => {
  if (err) {
    console.error(err);
    process.exit(1);
  }
  console.log(`server is running ${address}`);
});