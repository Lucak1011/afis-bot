const { REST, Routes } = require('discord.js')


module.exports = {
    data: new SlashCommandBuider()
        .setName('ping')
        .setDescription('Replies with pong'),
    async execute(interaction) {
        await interaction.reply('pong');
    },

};