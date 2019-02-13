export const groupByAuthor = (messages) => {
  const groupedMessages = [];

  for (const message of messages) {
    const lastMessage = groupedMessages[groupedMessages.length - 1];

    if (lastMessage && lastMessage.author === message.author) {
      lastMessage.messages.push(message.message);
    } else {
      groupedMessages.push({
        author: message.author,
        messages: [message.message],
      });
    }
  }

  return groupedMessages;
};
