const { Events } = require('discord.js');

module.exports = {
    async execute(interaction) {
        if (!interaction.isChatInputCommand()) return;

        const command = Interaction.client.commands.get(Interaction.commandName);

        if (!command) {
            console.error(`No command matching ${interaction.commandName} was found`);
            return;
        }
        try {
            await command.execute(interaction);
        } catch (error) {
            console.error(error);
            if (interaction.replied || interaction.deferred) {
                await interaction.followup({ content: 'There was an error while executing this command!', ephermal: true });
            } else {
                await interaction.reply({ content: 'There was an error while executing this command!', ephermal: true });
            }
        }
    }
}