class Api {
  constructor() {
    this.pool = {};

    this.SOURCE = './src/data';
    this.MESSAGES = `${this.SOURCE}/messages.json`;
  }


  async requestMessages() {
    if (this.pool[this.MESSAGES]) {
      return this.pool[this.MESSAGES];
    } else {
      const request = Api.requester(this.MESSAGES);

      this.pool[this.MESSAGES] = request;

      return request;
    }
  }

  static async requester(route) {
    return fetch(route).then((res) => {
      return res.json();
    });
  }
}

const api = new Api();

export default api;
