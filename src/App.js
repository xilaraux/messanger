import Display from './components/Display.js';

class App {
  mount(node) {
    if (!(node instanceof Node)) {
      throw new Error('Node should be instance of Node.');
    }

    const MessagesComponent = new Display().render();

    node.appendChild(MessagesComponent);
  }
}

const app = new App;

export default app;
