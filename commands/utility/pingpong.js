const { REST, Routes } = require('discord.js')

new SlashCommandBuider()
    .setName('ping')
    .setDescription('Replies with pong');

    async execute(interaction) {
    await interaction.reply('Pong!')
}
