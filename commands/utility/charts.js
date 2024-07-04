const { SlashCommandBuilder } = require('discord.js')
// options must be 1-32 chars and not contain caps

module.exports = {
    data: new SlashCommandBuilder()
        .setName('charts')
        .setDescription('Provides a chartfox link for aerodrome charts')
        .addStringOption(option =>
            option.setName('icao')
                .setDescription('Enter airport ICAO')
                .setRequired(true)),
    async execute(interaction) {
        const icaoCode = interaction.options.getString('icao')
        await interaction.reply({ content: `https://chartfox.org/${icaoCode}`, ephemeral: true })
    },

};