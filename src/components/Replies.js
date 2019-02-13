import { currentUser } from '../contants.js';

export default class Replies {
  constructor(props) {
    if (!props.messages) {
      throw new Error('Cannot render Replies without messages.');
    }

    this.isCurrentUser = props.author === currentUser;
    this.messages = props.messages;
  }

  render() {
    const repliesArea = document.createElement('article');

    for (const message of this.messages) {
      const replied = this.renderText(message);

      repliesArea.appendChild(replied);
    }

    if (this.isCurrentUser) {
      repliesArea.setAttribute('class', 'currentUser');
    }

    return repliesArea;
  }

  renderText(text) {
    const replied = document.createElement('p');
    replied.innerText = text;

    return replied;
  }
}
