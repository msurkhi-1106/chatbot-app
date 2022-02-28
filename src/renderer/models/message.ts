import { User } from './user';

export default class Message {
  date: Date;
  sender: User;
  message: string;

  constructor(date: Date, sender: User, message: string) {
    this.date = date;
    this.sender = sender;
    this.message = message;
  }
}
