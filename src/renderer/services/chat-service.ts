import Message from 'renderer/models/message';
import { Service } from './service';

export class ChatService extends Service {
  messageCallback = (messages: Message[]) => {};

  sendMessage(message: string) {
    this.messageCallback(this.messages);
    this.addMessage(new Message(new Date(), 'Jordan', message));
  }

  private addMessage(message: Message) {
    this.app.$store.commit('addMessage', message);
  }

  get messages() {
    return this.app.$store.getters['getMessages'];
  }
}
