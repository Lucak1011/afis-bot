const {SlashCommandBuilder, REST, Routes} = require('discord.js');
const request = require('request');


//command

module.exports = {
    data: new SlashCommandBuilder()
    .setName('metar')
    .setDescription('Pulls a METAR when an ICAO code is entered')
    .addStringOption(option =>
        option.setName('icao')
        .setDescription('Enter an ICAO code')
        .setRequired(true)),
    async execute(interaction){
        const icao = interaction.options.getString('icao').toUpperCase();

        let options = {
            'method': 'GET',
            'url': `https://metar.vatsim.net/${icao}`,
            'headers': {
                'Accept': 'text/plain'
            }
        };

        await interaction.deferReply();

        request(options, (error, response) =>{
            if (error) {
                console.error(error);
                interaction.editReply('There was an error fetching METAR data, try again later!');
                return;
            }

            interaction.editReply(`METAR data for ${icao}: \n\`\`\`${response.body}\`\`\``)
        });

    }
};