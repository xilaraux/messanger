import Replies from './Replies.js';

import Api from '../Api.js';
import { groupByAuthor } from '../utils.js';

export default class Display {
  constructor() {
    this.id = 'Display' + Math.random();
    this.fetchMessages(this.renderReplies);
  }

  render() {
    const displayNode = document.createElement('div');
    displayNode.setAttribute('id', this.id);

    return displayNode;
  }

  fetchMessages(cb) {
    Api.requestMessages().then(data => {
      const groupedMessages = groupByAuthor(data);

      cb.call(this, groupedMessages);
    });
  }

  renderReplies(replies) {
    const displayNode = document.getElementById(this.id);

    for (const replied of replies) {
      const RepliesComponent = new Replies(replied);

      displayNode.appendChild(RepliesComponent.render());
    }
  }
}
